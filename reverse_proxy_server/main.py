from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# CORS middleware to allow requests from your frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specify the domains you want to allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/heartbeat')
async def heartbeat():
    return {"status": "ok"}

@app.post("/find-similar")
async def proxy_find_similar(file: UploadFile = File(...)):
    url = "https/find-similar?top_k=20"
    files = {'file': (file.filename, file.file, file.content_type)}
    
    try:
        response = requests.post(url, files=files)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))
