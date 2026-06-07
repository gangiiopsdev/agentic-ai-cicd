from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = shlex.split(f'ping {host}')
    subprocess.run(args)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
    except Exception as e:
        return {'error': str(e)}
    return {'status': 'completed'}