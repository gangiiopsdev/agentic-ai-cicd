from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() and '-' not in host:
        return {'status': 'error', 'output': 'Invalid input'}
    try:
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)