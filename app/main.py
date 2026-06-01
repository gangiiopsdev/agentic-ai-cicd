from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if all(c.isalnum() or c in ['-', '.', '_', '\'] for c in host):
        return safe_ping(host)
    else:
        return {'error': 'Invalid input'}