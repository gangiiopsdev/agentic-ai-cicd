from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True, timeout=5)
    return result.stdout if result.returncode == 0 else result.stderr

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.TimeoutExpired as e:
        return {'status': 'failed', 'error': 'Timeout occurred'}