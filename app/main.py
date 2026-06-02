from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not host or len(host.split('.')) != 4 or any(not part.isdigit() for part in host.split()):
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=False)
        if result.returncode != 0:
            return {'status': 'completed', 'output': result.stderr}
        else:
            return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)