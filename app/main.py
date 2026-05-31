from fastapi import FastAPI, Depends
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
correct_username = "admin"

app = FastAPI()
security = HTTPBasic()

async def verify_password(username: str, password: str):
    return username == correct_username and password == "correct_password_hashed"

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(security)):
    if not await verify_password(credentials.username, credentials.password):
        return {'status': 'failed', 'error': 'Invalid credentials'}

    def safe_ping(host: str):
        # Whitelisted hosts or IP ranges
        allowed_hosts = ['127.0.0.1', '::1']
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            output = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

    return safe_ping(credentials.username)