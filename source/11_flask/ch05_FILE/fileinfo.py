# 특정 폴더(uploads) 안의 파일들의 정보를 listup
import os
import datetime

UPLOAD_FOLDER = './uploads/'

filelist = os.listdir(UPLOAD_FOLDER)
# print(filelist)

def stamp2datetime(stamp):
    return datetime.datetime.fromtimestamp(stamp)

def info(filename):
    ctime = os.path.getctime(UPLOAD_FOLDER + filename)
    mtime = os.path.getmtime(UPLOAD_FOLDER + filename)
    atime = os.path.getatime(UPLOAD_FOLDER + filename)
    size = os.path.getsize(UPLOAD_FOLDER + filename)
    if size >= 1024 * 1024:
        size = size / (1024 * 1024)
        size = '{:.3f}MB'.format(size)
    elif size >= 1024:
        size = size / 1024
        size = '{:.3f}KB'.format(size)
    else:
        size = '{}B'.format(size)

    return stamp2datetime(ctime), stamp2datetime(mtime), stamp2datetime(atime), size

if __name__ == '__main__':
    filelist = os.listdir(UPLOAD_FOLDER)
    for filename in filelist:
        ctime, mtime, atime, size = info(filename)
        print(filename, ctime, mtime, atime, size)