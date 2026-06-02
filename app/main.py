from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host: str):
    # Simple heuristic to prevent command injection
    if '||' in host or ';' in host or '&' in host:
        raise ValueError('Invalid input')
    return host

@app.get("/ping")
def ping(host: str):
    try:
        safe_host = escape_host(host)
        result = subprocess.run(['ping', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}