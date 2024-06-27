from msilib.schema import File

from fastapi import FastAPI, UploadFile, File
import uvicorn
from starlette.responses import RedirectResponse
from prediksi import breed_detector

app = FastAPI()

# @app.get('/index')
# def hello_world():
#     return "hello world!"

@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")

@app.post("/predict")
async def predict_image(file: UploadFile):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Foto harus dengan format jpg, jpeg, atau png"
    file_path = f"C:/Users/Dipa/Documents/Project Portofolio/dog breed classification api/foto/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    prediction = breed_detector(file_path)
    return prediction

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='localhost')
