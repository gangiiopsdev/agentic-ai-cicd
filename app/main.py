from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        args = ['ping', '-c', '4', host]
        return subprocess.call(args, shell=False)
    except Exception as e:
        raise ValueError('Invalid input for ping') from e

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