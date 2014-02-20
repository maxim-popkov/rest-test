from django.db import models

class Classifier(models.Model):
	title = models.CharField(max_length=64)
	desc = models.TextField()

class Label(models.Model):
	name = models.CharField(max_length=64)

class TrainVector(models.Model):
	cls = models.ForeignKey(Classifier)
	lbl = models.ForeignKey(Label)
	data = models.CharField(max_length=64)
