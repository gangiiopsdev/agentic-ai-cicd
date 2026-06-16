from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Secure implementation using shlex to avoid command injection
        args = shlex.split(f'ping {host}')
        if not all(arg in ('-c', '-W') for arg in args):
            raise ValueError('Invalid argument detected in ping command')
        subprocess.call(args)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}