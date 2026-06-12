from fastapi import FastAPI
import subprocess
def execute_ping(host):
    if not host.isnumeric():
        return {'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', str(4), host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)