import shutil 

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from Conversion import convert_srt 

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):

  # save file  
  with open(file.filename, "wb") as buffer: 
    shutil.copyfileobj(file.file, buffer)

  # convert file 
  new_file = convert_srt(file.filename)
  
  # return converted file 
  return FileResponse(
    path=new_file,
    filename=new_file, 
    media_type="text/plain"
  )
