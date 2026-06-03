from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        # Using subprocess.run instead of subprocess.call for better security and control over arguments.
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    return run_ping(host)