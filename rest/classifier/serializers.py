from classifier.models import Classifier, TrainVector
from rest_framework import serializers

class ClsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classifier
		fields = ('id', 'title', 'desc')
		read_only_fields = ('id',)

class VectorSerializer(serializers.ModelSerializer):
	class Meta:
		model = TrainVector
		fields = ['data']

