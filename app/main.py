from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Using subprocess.run for safer execution
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.decode('utf-8')}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)