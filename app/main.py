from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

given_host = '127.0.0.1' # Replace with a secure source of hostnames

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str): 
    try:
        # Validate the host input
        if not host.isnumeric() or int(host) > 255:
            return {"status": "error", "message": "Invalid host address"}
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}