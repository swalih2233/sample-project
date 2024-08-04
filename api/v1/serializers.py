from rest_framework import serializers
from app.models import Upload

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ('image', 'description')


