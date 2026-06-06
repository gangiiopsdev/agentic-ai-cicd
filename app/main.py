from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.exceptions import HTTPException

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.get("/ping")
def ping(host: str):\n    # Secure implementation\n    if not host.isdigit():\n        raise HTTPException(status_code=400, detail="Invalid host input")\n    subprocess.run(["ping", host], check=True)\n    return {"status": "completed"}