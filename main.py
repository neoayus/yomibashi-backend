from fastapi import FastAPI, UploadFile, File
import shutil 

# import conversion function 
from Conversion import convert_srt 

app = FastAPI()

# upload file 
# @app.post("/upload")
# def upload_file(file: UploadFile = File(...)):
#     return {"filename": file.filename}
  
@app.post("/upload")
async def upload(file: UploadFile = File(...)):

  # save file  
  with open(file.filename, "wb") as buffer: 
    shutil.copyfileobj(file.file, buffer)

  # convert file 
  new_file = convert_srt(file.filename)
  
  # return new file 
  return{
    "saved": file.filename, 
    "converted": new_file
  }
