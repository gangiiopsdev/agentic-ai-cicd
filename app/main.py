from fastapi import FastAPI
import subprocess
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

global_host_whitelist = {'google.com', 'example.com'}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping(host: str):
    if host not in global_host_whitelist:
        return {"status": "error", "message": "Unauthorized host"}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "result": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}