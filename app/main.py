from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI()
security = HTTPBasic()

@app.get("/ping")
def ping(host: str = Depends(security)):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}

@app.exception_handler(HTTP_401_UNAUTHORIZED)
def handle_unauthorized_exception(request, exc):
    return HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Invalid credentials")