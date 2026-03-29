import fastapi.responses
import shutil
import os

from fastapi import APIRouter,UploadFile,File
from fastapi.responses import FileResponse

router=APIRouter(prefix='/file',tags=['file'])

@router.post('/1')
def get_file(file:bytes=File(...)):
    content=file.decode('utf-8').split("\r\n")
    return content

#@uploadfile is wrapper of file 
@router.post('/2')
def get_file_by_uploadfile(upload_file:UploadFile=File(...)):
    path=f'./Files_S10/{upload_file.filename}'
    
    with open(path,"wb") as f:
        #shutil is a built-in Python module for high-level file operations. shell utilities → shutil
        shutil.copyfileobj(upload_file.file,f)
        
        # with open(path, "wb") as f:
        #     f.write(upload_file.file.read())
        #         ✔ Simple
        #         ✖ If the file is large (1GB), your RAM will cry
        #         ✖ Not recommended for production
        #           with open(path, "wb") as f:
                    # await upload_file.write(f)
    return {
        "filename":upload_file.filename,
        "type":upload_file.content_type
    }
    
    
#     ✅ 1. What does app.mount() mean?
# app.mount() tells FastAPI:

# “Attach another small application at this specific URL path.”

# So FastAPI can serve:

# Main API endpoints
# Plus another folder containing files (images, PDFs, uploads, CSS, etc.)

# Think of it like attaching a USB drive to your computer → now you can access its files.

# ✅ 2. What does StaticFiles do?
# StaticFiles is a helper class that serves a folder of files directly to the browser.
# For example, if you have:
# files/
#     photo.jpg
#     doc.pdf
#     hello.txt

# FastAPI can serve these files like a web server.


#  /Files_S10
# This is the URL path where files will be available.
# Users can visit:
# http://localhost:8000/Files_S10/photo.jpg

# 🔹 directory="files"
# This is the folder on your computer that contains the files.
# So FastAPI looks inside:
# your_project_folder/
#     main.py
#     files/   <--- this folder is mapped

# 🔹 name="files"
# This is just an internal name used inside FastAPI.
# (Not important for basic use.)


@router.get('/download/{name}')
def download_file(name:str):
    path=f'Files_S10/{name}'
    if not os.path.exists(path):
        return f"Error: {name} file not found"
    
    return FileResponse(path,media_type='application/pdf',filename=name)