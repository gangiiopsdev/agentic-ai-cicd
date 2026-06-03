from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the host input using shlex.quote
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)