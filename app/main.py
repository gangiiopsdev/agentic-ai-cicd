from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
            return {'status': 'failed', 'stderr': 'Invalid hostname'}
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'stderr': str(e)}