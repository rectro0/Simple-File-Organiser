import os
from pathlib import Path 
import shutil



def main():
 filePath = input("Paste your Folder path here --> ") 
 Download_path = Path(filePath)


 files = {
  "PDFs": Download_path / "PDFs",
    "Images": Download_path / "Images",
    "Archives": Download_path / "Zip",
    "Videos" : Download_path / "Videos",
    "Music": Download_path / "Audio",
    "Documents": Download_path / "Document",
    "Torrents": Download_path / "torrents",
    "others" : Download_path / "others",
 }

 file_type = {
   'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.xls', '.mdb', '.mpp', '.doc', '.xml', '.ppt', '.docx', '.txt'],
    'Videos': ['.mp4', '.mkv'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar'],
    'PDFs': ['.pdf'],
    'Torrents': ['.torrent'],
    'others' : [],
 }


 for  file in files.values() :
  try:
   file.mkdir()
  except FileExistsError  :
   print(f"{file} already exists!!") 





 for  item in Download_path.iterdir():
  if item.is_file():
   name , exten = os.path.splitext(item.name)
   exten = exten.lower()
   print(f'file names : {name} , file extenion : {exten}\t')
   moved= False
   for name , extention in file_type.items():
    if exten in extention:
     dest = files[name] / item.name
     if not dest.exists():
      shutil.move(str(item), str(files[name] / item.name))
      print(f'Moved {item.name} to {files[name]}')
      moved= True
     else:
      print(f'{dest} already exists , skipped!' )
      moved = True
      break
   if not moved:
     dest = files['others'] / item.name
     if not dest.exists():
      print(f'Unknown file Type for {item.name} , Moved to Others')
      shutil.move(str(item) , str(files['others']))
     else:
      print(f'{dest} already exists , skipped!')

if __name__ == "__main__":
   main()

 
 
 
 
 
   