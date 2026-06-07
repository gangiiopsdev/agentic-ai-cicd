from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import JSONResponse

app = FastAPI()
security = HTTPBasic()

async def authenticate(credentials: HTTPBasicCredentials):
    correct_username = credentials.username == "admin"
    correct_password = credentials.password == "secret"
    if not (correct_username and correct_password):
        return False
    return credentials

@app.get("/ping")
def ping(host: str, credentials: HTTPBasicCredentials = Depends(authenticate)):
    try:
        result = subprocess.run(["ping", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return JSONResponse(content={"status": "completed", "stdout": result.stdout}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"status": "error", "stderr": e.stderr}, status_code=500)