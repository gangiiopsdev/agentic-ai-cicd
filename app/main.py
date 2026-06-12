from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input detected')
    return safe_ping(shlex.quote(host))