from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), host: str = None):
    if not host:
        return {"status": "failed", "error": "Host parameter is required"}
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.run(['ping', '-c', '1', f'--{sanitized_host}'], capture_output=True, text=True, check=True, shell=False, cwd='/safe/directory')
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}