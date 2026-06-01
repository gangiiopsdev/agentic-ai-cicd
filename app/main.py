from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping")
def ping(host: str):  # Use Pydantic model to validate input
    if not host.isalnum():  # Basic validation of the hostname
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)  # Use '-c' option for number of pings and specify full command
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}