from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid host name")

app = FastAPI()

@app.get("/ping/{host}")
def ping(host: str):
    try:
        output = subprocess.run(['ping', '-c', '1', safe_ping(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}