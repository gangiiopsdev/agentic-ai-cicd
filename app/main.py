from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    # Basic check for safe characters in hostname
    return all(c.isalnum() or c in ['-', '_'] for c in hostname)

@app.get="/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        return {"status": "failed", "error": "Invalid hostname"}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode('utf-8')}