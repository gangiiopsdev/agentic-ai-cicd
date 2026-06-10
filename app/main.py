from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

async def authenticate(credentials: HTTPBasicCredentials):
    correct_username = credentials.username == 'admin'
    correct_password = credentials.password == 'secret'
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=401,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Basic realm="Admin Area"'},
        )
    return credentials

@app.get("/ping")
def ping(host: str = Depends(authenticate)):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}