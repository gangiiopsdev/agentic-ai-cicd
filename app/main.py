from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host.isalnum() and len(host) <= 255:
        try:
            result = subprocess.run(shlex.split(f"ping {host}"), capture_output=True, text=True, timeout=10)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.TimeoutExpired:
            return {'error': 'Ping request timed out'}
    else:
        return {'error': 'Invalid input'}