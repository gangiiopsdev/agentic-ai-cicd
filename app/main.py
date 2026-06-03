from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI()
security = HTTPBasic()

def is_safe_host(host):
    # Implement logic to validate the host input against a whitelist of allowed hosts
    return host in ['safehost1', 'safehost2']

@app.get("/ping")
def ping(host: str = Depends(security)):
    if not is_safe_host(host):
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}

@app.exception_handler(HTTP_401_UNAUTHORIZED)
def handle_unauthorized_exception(request, exc):
    return HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Invalid credentials")