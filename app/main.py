from fastapi import FastAPI
import subprocess
from os import getpass
getpass = __import__(getpass)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run to avoid shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}