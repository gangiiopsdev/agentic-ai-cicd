from fastapi import FastAPI
import subprocess

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    command = ['ping', host]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}