from fastapi import FastAPI
import subprocess
def run_safe_ping(host):
    args = ['ping', host]
    return subprocess.run(args, capture_output=True, text=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if '127.0.0.1' not in host and 'localhost' not in host:
        raise ValueError("Invalid host")
    result = run_safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}