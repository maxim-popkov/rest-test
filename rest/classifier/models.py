from django.db import models


class Classifier(models.Model):

    """
    DataBase ORM Model for Classifier
    """
    title = models.CharField(max_length=64)
    desc = models.TextField()
    save_file_path = models.FileField(upload_to='cls', blank=True)

    def __unicode__(self):
        return self.title


class Label(models.Model):
    
    """
    DataBase ORM Model for Label
    """
    
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class TrainVector(models.Model):

    """
    DataBase ORM Model for Train Vector
    """
    
    cls = models.ForeignKey(Classifier)
    lbl = models.ForeignKey(Label)
    data = models.TextField()

    def __unicode__(self):
        return self.data


class TestVector(models.Model):
    
    """
    DataBase ORM Model for Test Vector
    """
    
    # param blank=True for admin panel,
    # with param can add vector without specifying foreignkeys
    cls = models.ForeignKey(
        Classifier, null=True, blank=True, db_constraint=False)
    lbl = models.ForeignKey(Label, null=True, blank=True, db_constraint=False)
    data = models.TextField()
    isClassified = models.BooleanField(default=False)

    def __unicode__(self):
        return self.data
