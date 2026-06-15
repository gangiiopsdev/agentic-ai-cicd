from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Add more allowed hosts as needed
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), host: str = None):
    if not host:
        return {"status": "failed", "error": "Host parameter is required"}
    try:
        validate_host(host)
        sanitized_host = sanitize_input(host)
        output = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True, shell=False, cwd='/safe/directory')
        return {"status": "completed", "output": output.stdout}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}