import os

#directory_path를 기준으로 그 안에 있는 파일들의 정보를 전부 가져온다. 
def list_files_in_directory(directory_path):
    entries = os.listdir(directory_path)
    
    files = [entry for entry in entries if os.path.isfile(os.path.join(directory_path, entry))]
    
    return files

#지금 나의 경로를 가져온다. 
def find_now_directory():
    return os.getcwd()