from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(security)):
    host = credentials.username  # Assuming the username contains the host to ping
    if not host or not host.strip():
        return {'error': 'Invalid input'}, 400

    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}