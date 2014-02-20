from django.contrib import admin
from classifier.models import TestVector, TrainVector, Classifier, Label


def classify(modeladmin, request, queryset):
	queryset.update(isClassified=True)

classify.short_description = "Classify selected objects"

class TestVectorAdmin(admin.ModelAdmin):
	list_display = ['isClassified','cls','lbl','data']
	actions = [classify]

admin.site.register(TestVector, TestVectorAdmin)
admin.site.register(TrainVector)
admin.site.register(Classifier)
admin.site.register(Label)