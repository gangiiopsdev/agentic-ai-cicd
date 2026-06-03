from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using subprocess.run instead of subprocess.call
    try:
        subprocess.run(['ping', host], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}