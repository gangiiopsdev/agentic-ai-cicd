from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate host input
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout,

app = FastAPI()
@app.get("/ping")
def ping(host: str):    return {'status': 'completed', 'output': safe_ping(host)}