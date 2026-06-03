from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Validate and sanitize host input
    if not host.isdigit() or len(host) > 3:
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get('/ping')
def ping(host: str):\n    try:\n        safe_ping(host)\n        return {'status': 'completed'}\n    except subprocess.CalledProcessError as e:\n        return {'error': str(e)}