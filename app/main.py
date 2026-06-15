from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run without shell=True
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode('utf-8'), 'stderr': result.stderr.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'stdout': '', 'stderr': str(e)}

@app.get("/ping")
def ping_handler(host: str):
    result = ping(host)
    return result