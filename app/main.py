from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(shlex.split('ping {}'.format(host)), capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result is None:
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed', 'output': result}