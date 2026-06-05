from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI()
security = HTTPBasic()

def verify_password(username: str, password: str):
    return username == "admin" and password == "secret"

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(security), host: str = Depends(lambda _: _)):
    if verify_password(credentials.username, credentials.password):
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")