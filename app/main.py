from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Safe implementation using subprocess.run and shell=False
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}