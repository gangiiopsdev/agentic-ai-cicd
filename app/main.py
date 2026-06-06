from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not isinstance(host, str) or ' ' in host:
        raise ValueError('Invalid host name')
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}