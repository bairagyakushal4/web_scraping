import os
import shutil
# install calibre
# pip install capybre
from capybre import convert


allDoc = [file for file in os.listdir() if file.endswith(".docx")]

if allDoc == []:
    exit()


os.mkdir('epub')

for d in allDoc:
    FileFullName = os.path.basename(d)
    # doc_split = os.path.splitext()
    # doc_only_name = doc_split[0]    

    newFile = convert(FileFullName, as_ext='epub')
    new_path = 'epub/' + newFile
        
    shutil.move(newFile, new_path)
    
    print(new_path)
