from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        if not host.isalnum():
            raise HTTPException(status_code=400, detail="Invalid input")
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
or
from fastapi import FastAPI, HTTPException
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        if not re.match(r'^[a-zA-Z0-9]+$', host):
            raise HTTPException(status_code=400, detail="Invalid input")
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}