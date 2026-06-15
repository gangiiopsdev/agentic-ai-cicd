from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    # Sanitize the host input to avoid shell injection
    safe_host = shlex.quote(host)
    try:
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}

@app.get="/ping")
def ping(host: str):
    return secure_ping(host)