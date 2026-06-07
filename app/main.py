from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host or len(host) > 255 or ' ' in host:
            raise ValueError('Invalid host input')
        subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    return safe_ping(host)