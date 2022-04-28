import datetime
import random

"""
ckeditor4에서 파일을 업로드시 같은 폴더에 같은 파일명이 생기지 않도록 하는것

"""
def get_filename(filename):
    string = "asdf"
    for i in range(1,20):
        string+=str(random.randrange(0,10))
        
    return filename.upper()+string