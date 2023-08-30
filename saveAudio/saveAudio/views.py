# import os
# from django.http import JsonResponse
# from django.core.files.storage import FileSystemStorage
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import parser_classes
# from rest_framework.parsers import FormParser
# from rest_framework.parsers import MultiPartParser
# from saveAudio.models import *
# import filetype

# @csrf_exempt
# @parser_classes([FormParser, MultiPartParser])
# def upload_file(request):
#     if request.method == 'POST':
#         uploaded_file = request.FILES['form_file']

#         storage = FileSystemStorage()
#         filename = storage.save(uploaded_file.name, uploaded_file)
#         saved_file_path = storage.url(filename)
#         file_path = f'../saveAudio/{saved_file_path}'
#         file_size = os.stat(file_path)
#         formatted_size = (format_size(file_size.st_size))

#         kind = filetype.guess(uploaded_file)
#         print(kind.extension)
#         print('DONE')
#         save_data = FileDataHandle(uploaded_file.name )
#         save_data.save()
#         return JsonResponse({'message : Done:' : saved_file_path})
#     else: 
#        # Get the raw request body as bytes
#         raw_body = request.body
#         print('NOT DONE')
        
#     # Convert bytes to a string (assuming it's a valid string)
#         body_as_string = raw_body.decode('utf-8')

#     # Print the request body for debugging
#         print(body_as_string)        
#         return JsonResponse({'message': 'File upload failed'}, status = 400)


# def format_size(size):
#  for unit in ['B', 'KB']:
#    if size < 1024:
#        return f"{size:.2f} {unit}"
#    size /= 1024