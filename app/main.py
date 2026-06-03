from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if 'ping' in host or host.startswith('-'):
        return "Invalid input"
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)