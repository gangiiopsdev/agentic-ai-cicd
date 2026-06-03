from fastapi import FastAPI, HTTPException
import subprocess
import re

app = FastAPI()

def sanitize_host(host):
    return re.sub(r'[^a-zA-Z0-9]', '', host)

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
        if not sanitized_host.isalnum():
            raise HTTPException(status_code=400, detail="Invalid input")
        output = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}