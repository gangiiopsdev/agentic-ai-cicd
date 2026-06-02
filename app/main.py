from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Validate input to prevent command injection
        if not all(c.isalnum() or c in '._-' for c in host):
            return {'status': 'failed', 'stderr': 'Invalid hostname'}
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'stderr': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)