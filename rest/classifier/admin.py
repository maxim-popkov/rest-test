from django.contrib import admin
from classifier.models import TestVector, TrainVector, Classifier, Label
import logging
import classify_master as cm
import json


def get_docs(db_vectors):
    """
    Get data from db_vectros to array docs
    """
    docs = []
    categories = []
    for vector in db_vectors:
        data = vector.data
        label = vector.lbl.name if vector.lbl else None
        doc = json.loads(data)
        docs.append(doc)
        categories.append(label)
    return docs, categories


def classify(modeladmin, request, queryset):
    queryset.update(isClassified=True)
    logging.info(str(queryset))
    logging.info(type(queryset[0]))

    raw_train_vectors = TrainVector.objects.all()
    raw_test_vectors = TestVector.objects.all()
    raw_categories = [name for name in Label.objects.all()] 

    train_docs, train_labels = get_docs(raw_train_vectors)
    test_docs, tmp = get_docs(raw_test_vectors)

    logging.info(test_docs)
    logging.info(train_docs)
    logging.info(train_labels)

    train_set = cm.weight_train_vectors(train_docs)
    test_set = cm.weight_test_vectors(test_docs)
    cm.train(train_set, train_labels)
    predict_labels = cm.predict(test_set)

    logging.info(predict_labels)
    lbl = predict_labels[0]
    db_test_vector = raw_test_vectors[0]
    db_predicted_label = Label.objects.filter(name=lbl)[0]
    db_test_vector.lbl = db_predicted_label
    db_test_vector.save()

    # logging.error("this is an error!")

classify.short_description = "Classify selected objects"


class TestVectorAdmin(admin.ModelAdmin):
    list_display = ['isClassified', 'cls', 'lbl', 'data']
    actions = [classify]

admin.site.register(TestVector, TestVectorAdmin)
admin.site.register(TrainVector)
admin.site.register(Classifier)
admin.site.register(Label)
