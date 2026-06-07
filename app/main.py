from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host == 'localhost':
        return {'status': 'completed', 'output': ''}
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', safe_ping(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}