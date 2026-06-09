from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
def safe_ping(host: str):
    if not host.isalnum():
        return JSONResponse(status_code=400, content={'error': 'Invalid host name'})
    args = ['ping', host]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return JSONResponse(content={'status': 'success', 'output': result.stdout.decode('utf-8')})

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)