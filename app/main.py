from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using check_output and shell=False
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}