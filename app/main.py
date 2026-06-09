from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Secure implementation using shlex.split to prevent command injection
        subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}