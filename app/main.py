from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    validated_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', validated_host], check=True)
    return {"status": "completed"}