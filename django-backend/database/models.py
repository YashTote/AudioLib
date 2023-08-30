from django.db import models

# Create your models here.
from datetime import date


class FileDataHandle(models.Model):
    '''
    Django DB model to store the meta data in SQLite database.

    The model does not store the audio file but infact stores the file location.

    The audio files are stored inside Media folder of the Django App.
    '''
    file_name = models.CharField(max_length=40)
    file_type = models.CharField(max_length=10)
    file_location = models.CharField(max_length=100)
    file_size = models.CharField(max_length=20)
    date_time = models.DateTimeField(default=date.today)

    # def __str__(self):
    #     return f'{self.file_name}-{self.file_type}-{self.file_size}'
    
class FileName(models.Model):
    nameZone = models.CharField(max_length=5)
  