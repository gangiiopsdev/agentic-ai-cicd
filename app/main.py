from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
security = HTTPBasic()

generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/ping')
def ping(credentials: HTTPBasicCredentials = Depends(security)):
    subprocess.run(generate_ping_command(credentials.username), shell=False, check=True)
    return {'status': 'completed'}