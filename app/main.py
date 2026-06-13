from fastapi import FastAPI
import subprocess
get = app.get

global app
app = FastAPI()

@get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}