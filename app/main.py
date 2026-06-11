from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    return safe_ping(host)

def is_safe_host(host: str):
    # Implement logic to validate the host
    return True