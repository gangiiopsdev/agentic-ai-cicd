from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

def safe_ping(host: str):
    try:
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        args = ['ping', shlex.quote(host)]  # Use shlex.quote to safely escape the input
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)