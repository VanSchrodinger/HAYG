# #目录更新
import os
from .models import FileInfo
from 

def update_folder():
    index_path='Z:\\PYTHON_FILE\\wansx\\'
    file_list=os.listdir(index_path)
    had_files=FileInfo.objects.values_list('file_path',flat=True)
    for file_folder in file_list:
        if os.path.isdir(os.path.join(index_path, file_folder)):
            if os.path.join(index_path, file_folder) not in had_files:
                file_info = FileInfo(file_name=file_folder, 
                        file_size=0, 
                        file_path=os.path.join(index_path, file_folder),
                        file_type='FOLDER',
                        load_user='wansx',
                        is_personal=1,
                        folder_name=index_path)                  
                file_info.save()
                file_size1=os.path.getsize(os.path.join(index_path, file_folder))
                FileInfo.objects.filter(file_path=os.path.join(index_path, file_folder)).update(file_size=1 if 0 < file_size1 < 1024 else file_size1 / 1024)
        else:
            if os.path.join(index_path, file_folder) not in had_files:
                file_info = FileInfo(file_name=file_folder, 
                        file_size=0, 
                        file_path=os.path.join(index_path, file_folder),
                        file_type=file_folder.split('.')[-1],
                        load_user='wansx',
                        is_personal=1,
                        folder_name=index_path)
                file_info.save()
                file_size1=os.path.getsize(os.path.join(index_path, file_folder))
                FileInfo.objects.filter(file_path=os.path.join(index_path, file_folder)).update(file_size=1 if 0 < file_size1 < 1024 else file_size1 / 1024)

