from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate input to prevent command injection
    if not host.strip() or '&&' in host or ';' in host or '|' in host:
        raise ValueError('Invalid host parameter')
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {
            "status": "completed",
            "stdout": result.stdout.decode(),
            "stderr": result.stderr.decode()
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "stdout": e.stdout.decode() if e.stdout else '',
            "stderr": e.stderr.decode() if e.stderr else ''
        }

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)