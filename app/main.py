from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    try:
        result = subprocess.run(['ping'] + [shlex.quote(arg) for arg in shlex.split(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode('utf-8')}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)