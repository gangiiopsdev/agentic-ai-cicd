from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host):
    # Secure implementation using subprocess.run with proper argument quoting and validation
    if not host or not host.isalnum():
        raise ValueError('Invalid input')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    status = execute_ping(host)
    return {'status': 'completed', 'output': status}