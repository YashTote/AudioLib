import os
from django.http import JsonResponse, FileResponse, StreamingHttpResponse
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
from .serializer import *
from .models import *
import filetype


@csrf_exempt
@parser_classes([FormParser, MultiPartParser])
@api_view(['GET','POST'])
def upload_file(request):
    '''
    This is the main view function of the application.

    Only the audio file is sent here from the FrontEnd. The neccessary Meta Data is created here and sent to the Database model after serialisation.  
    
    The audio files are saved in the local file storage, in the file named media at the root of the this application.

    The filetype dependency to get the extension of the incoming audio file. 
    '''
    if request.method == 'POST':
        uploaded_file = request.FILES['form_file']

        storage = FileSystemStorage()
        filename = storage.save(uploaded_file.name, uploaded_file)
        '''
        Most of the meta data is calculate here and then sent to the database mode.
        '''
        saved_file_path = storage.url(filename)
        file_path = f'../django-backend/{saved_file_path}'
        file_size = os.stat(file_path)
        formatted_size = (format_size(file_size.st_size))
        kind = filetype.guess(uploaded_file)

      
        file_data = FileDataHandle(
            file_name=uploaded_file.name,
            file_type=kind.extension,
            file_location=file_path,
            file_size=formatted_size
        )

        file_data.save()
        fileDesc = FileDataHandle.objects.filter(file_location = file_path)
        serialized_data = FileSerializer(fileDesc, many = True)
        return Response(serialized_data.data)
        
    elif request.method == 'GET':
       '''
       The incoming GET request is responded with the meta data of all the files that are present in the database. 

       '''
       fileList = FileDataHandle.objects.all()
       serialized_data = FileSerializer(fileList, many = True)
       return Response(serialized_data.data)

    else:         
        return JsonResponse({'message': 'File upload failed'}, status = 400)

@csrf_exempt
@parser_classes([FormParser, MultiPartParser])
@api_view(['GET','POST'])
def get_one_file(request, location):
   '''
   This method handles the incoming GET request, in response send a downloadble audio file.
   '''
   location = f'../django-backend//media/{location}'
   returnResponse = FileResponse(open(location, 'rb'))
   returnResponse['Content-Disposition'] = f'attachment; filename="{location}"'
   return returnResponse

def format_size(size):
 '''
 The audiofile has default size in bits which later is converted into MegaBytes here and returned. 
 '''
 mb_value = size / (1024 * 1024)
 return (f"{mb_value:.2f} MB")
   