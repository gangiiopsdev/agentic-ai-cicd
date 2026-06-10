from fastapi import FastAPI
import subprocess

def run_ping(host: str):
    safe_host = subprocess.shlex_quote(host)
    try:
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return run_ping(subprocess.shlex_quote(host))