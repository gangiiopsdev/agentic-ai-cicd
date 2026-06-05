from fastapi import FastAPI
import subprocess
def safe_ping(host):
    cmd = ['ping', '-c', '1', host]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)