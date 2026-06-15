from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str):\n    # Secure implementation\n    if not host.isalnum():\n        return {"error": "Invalid host name"}\n    subprocess.run(['ping', host], check=True)\n    return {"status": "completed"}