from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()

class PingRequest(BaseModel):
    host: str

def validate_host(host):
    # Simple validation to allow only alphanumeric and some special characters
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)

@app.post("/ping")
async def ping(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    if not validate_host(username):
        return JSONResponse(status_code=400, content={'status': 'error', 'message': 'Invalid host name'})
    try:
        result = subprocess.run(['ping', '-c', username], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=400, content={'status': 'error', 'message': str(e)})

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}