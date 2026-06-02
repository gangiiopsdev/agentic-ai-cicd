from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI()
security = HTTPBasic()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input sanitization
    if not host.isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/protected')
def protected_route(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "secret"
    if credentials.username == correct_username and credentials.password == correct_password:
        return {'message': 'Access granted'}
    else:
        return HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail='Incorrect username or password', headers={'WWW-Authenticate': 'Basic realm="Admin"'})