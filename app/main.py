from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    return ''.join(e for e in host if e.isalnum() or e in ['.', '-'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if 'ping' not in sanitized_host and '.' in sanitized_host:
        try:
            result = subprocess.run(['ping', '-c', 1, sanitized_host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}
    else:
        return {"status": "invalid_host"}