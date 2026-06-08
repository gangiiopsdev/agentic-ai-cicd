from fastapi import FastAPI
import subprocess
def run_ping(host):
    if not host.isnumeric():
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        run_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}