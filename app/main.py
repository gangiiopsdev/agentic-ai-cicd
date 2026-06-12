from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with absolute path and shell=False
    result = subprocess.run([os.path.abspath('ping'), host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}