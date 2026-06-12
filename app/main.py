from fastapi import FastAPI, HTTPException
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and validation of input
    if not re.match(r'^[a-zA-Z0-9]{1,255}$', host):
        raise HTTPException(status_code=400, detail="Invalid hostname")
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=False)
    return {
        "status": "completed",
        "output": result.stdout if result.returncode == 0 else result.stderr
    }