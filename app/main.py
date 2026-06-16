from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        subprocess.run(['ping', host], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
        return False

@app.get("/ping")
def ping(host: str):
    if execute_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}