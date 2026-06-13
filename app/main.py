from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with proper sanitization
    quoted_host = shlex.quote(host)
    try:
        result = subprocess.run(['ping', quoted_host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)