from django.db import models

class Classifier(models.Model):
	title = models.CharField(max_length=64)
	desc = models.TextField()

	def __unicode__(self):
		return self.title

class Label(models.Model):
	name = models.CharField(max_length=64)

	def __unicode__(self):
		return self.name

class TrainVector(models.Model):
	cls = models.ForeignKey(Classifier)
	lbl = models.ForeignKey(Label)
	data = models.CharField(max_length=64)

	def __unicode__(self):
		return self.data

class TestVector(models.Model):
	#param blank=True for admin panel, 
	#with param can add vector without specifying foreignkeys
	cls = models.ForeignKey(Classifier, null=True, blank=True, db_constraint=False)
	lbl = models.ForeignKey(Label, null=True, blank=True, db_constraint=False)
	data = models.CharField(max_length=64)
	isClassified = models.BooleanField(default=False)

	def __unicode__(self):
		return self.data