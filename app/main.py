from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get('/ping')
def ping(host: str = Query(..., min_length=1, max_length=255)):
    # Secure implementation
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}