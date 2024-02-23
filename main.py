import folderReadAPI

def main():
    ## 기본으로 가져가는 hello 함수 #불필요###
    # print("hello")
    
    ## folderReadAPI.find_now_directory()를 통해 실행 py의 경로를 확인하고, folderReadAPI.list_files_in_directory를 통해 파일들을 리스트로 가져옴 그리고 print함## 
    # print(folderReadAPI.list_files_in_directory(folderReadAPI.find_now_directory()))
    
    ##test.txt -> demon.txt -> test.txt##
    # folderReadAPI.set_file_title("test.txt", "demon.txt")
    # folderReadAPI.set_file_title("demon.txt", "test.txt")
    
    ## extract_fileextension_checker를 사용한 기능 체크 ##
    for match in folderReadAPI.list_files_in_directory(folderReadAPI.find_now_directory()):
        if(folderReadAPI.extract_fileextension_checker(match)):
            print(match)
    
if __name__ == "__main__":
    main()