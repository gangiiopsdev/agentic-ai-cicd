from fastapi import FastAPI
import subprocess
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "result": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}