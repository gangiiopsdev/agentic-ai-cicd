from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if 'ping' not in host:
        return False
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}