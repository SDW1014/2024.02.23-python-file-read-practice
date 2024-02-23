import folderReadAPI

directory_path = ''

def main():
    #print("hello")
    print(folderReadAPI.list_files_in_directory(folderReadAPI.find_now_directory()))
    
    
if __name__ == "__main__":
    main()