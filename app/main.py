from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode('utf-8'), 'stderr': result.stderr.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)