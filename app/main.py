from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts

@app.get("/ping")
def ping(host: str):
    if host in allowed_hosts:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'stdout': result.stdout}
    else:
        raise ValueError('Host not allowed')