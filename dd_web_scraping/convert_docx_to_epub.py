import os
# install calibre
# pip install capybre
from capybre import convert


allDoc = [file for file in os.listdir() if file.endswith(".docx")]

for d in allDoc:
    FileFullName = os.path.basename(d)
    # doc_split = os.path.splitext()
    # doc_only_name = doc_split[0]

    convert(FileFullName, as_ext='epub')
    print(FileFullName)
