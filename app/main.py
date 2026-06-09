from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Error pinging {host}: {e.stderr}')
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host.replace(' ', '')):
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'message': 'Ping failed'}