from rest_framework import serializers
from .models import *

class FileSerializer(serializers.ModelSerializer):
  '''
  DRF serializer that does the usual work of converting incoming data to pythons native Data Types.
  '''
  class Meta:
    model = FileDataHandle
    fields = '__all__'
    def __str__(self):
      return self.name