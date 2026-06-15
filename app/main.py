from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    return not host or ' ' in host

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        return {'status': 'error', 'output': 'Invalid input'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}