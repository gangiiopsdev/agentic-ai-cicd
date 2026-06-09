from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Using subprocess.run for a safer approach with shlex
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Using the safe function defined above
    status = safe_ping(host)
    return {'status': 'completed', 'result': status}