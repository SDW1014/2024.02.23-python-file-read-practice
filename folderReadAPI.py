import os

def list_files_in_directory(directory_path):
    entries = os.listdir(directory_path)
    
    files = [entry for entry in entries if os.path.isfile(os.path.join(directory_path, entry))]
    
    return files