from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host or len(host) > 255:
        raise ValueError('Invalid input for ping')
    try:
        args = ['ping', '-c', '4', host]
        return subprocess.call(args, shell=False)
    except Exception as e:
        raise ValueError('Invalid input for ping') from e

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        if result == 0:
            return {'status': 'success', 'message': 'Ping completed'}
        else:
            return {'status': 'error', 'message': 'Ping failed'}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}