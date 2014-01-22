from service.models import Document
from rest_framework import serializers

class DocSerializer(serializers.ModelSerializer):
	class Meta:
		model = Document
		fields = ('title', 'text', 'author')
