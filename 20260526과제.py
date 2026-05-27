dir1 = input("첫번째 디렉토리 이름 입력: ")
dir2 = input("두번째 디렉토리 이름 입력: ")
import os
def get_file(path):
    file_dict = {}
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                file_size = entry.stat().st_size
                with open(entry.path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()


                    file_dict[entry.name] = (file_size, content)
        return file_dict
def compare(dir1, dir2):
    info1 = get_file(dir1)
    info2 = get_file(dir2)
    if len(info1)!=len(info2):
        print("len 다름")
        return False
    files1 = set(info1.keys())
    files2 = set(info2.keys())

    if(files1 != files2):
        print("이름 다름.")
        return False
    for file_name in files1:
        size1, content1 = info1[file_name]
        size2, content2 = info2[file_name]

        if(size1 != size2):
            print("크기 다름")
            return False
        if(content1!=content2):
            print("파일 내용 다름")
            return False
    print("일치함.")
    return True
path_a = os.path.join(".",dir1)
path_b = os.path.join(".",dir2)

if(os.path.exists(path_a) and os.path.exists(path_b)):
    compare(path_a,path_b)
else:
    print("error")