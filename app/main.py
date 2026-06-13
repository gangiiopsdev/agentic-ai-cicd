from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

async def verify_password(username: str, password: str):
    # Replace with actual authentication logic
    return username == 'admin' and password == 'secret'

@app.get('/ping')
def ping(credentials: HTTPBasicCredentials = Depends(security)):
    if not await verify_password(credentials.username, credentials.password):
        raise HTTPException(status_code=401, detail='Incorrect email or password', headers={'WWW-Authenticate': 'Basic realm="secret"'})

    host = credentials.username
    # Sanitize user input
    safe_host = ''.join(filter(str.isalnum, host))
    result = subprocess.run(['ping', '-c 1', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}