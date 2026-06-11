from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return False
    try:
        subprocess.run(['ping', *host.split()], check=True, shell=False)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping command failed with error: {e}')
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'reason': 'Invalid host'}