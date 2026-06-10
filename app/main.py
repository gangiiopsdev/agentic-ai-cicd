from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)