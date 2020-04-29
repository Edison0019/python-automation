#This program is for backing up files within folders to zip files
#every time the program is executed the zip will be created on the current working directory
import zipfile,os,pathlib #this for creating paths for both unix and MS dos operating systems

def zipf(folder):
    path = os.path.abspath(pathlib.Path(folder))
    with zipfile.ZipFile('newfile.zip','w') as zfile:
        for foldername, subfoldernale,filename in os.walk(folder):
            for files in filename:
                filepath = os.path.join(foldername,files)
                zfile.write(filepath)
    print('done')