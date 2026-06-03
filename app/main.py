from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    # Sanitize input to prevent injection
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid host input')
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)