from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    # Validate the host to ensure it's a valid IP or hostname
    if not (host.replace('.', '', 3).isdigit() or '.' in host):
        raise ValueError('Invalid host format')
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)