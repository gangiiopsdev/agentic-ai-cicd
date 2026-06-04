from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isnumeric():
        cmd = ['ping', '-c', '1', host]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}