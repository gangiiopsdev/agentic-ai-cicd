from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Using shlex to safely parse the command arguments
        args = shlex.split(f'ping {host}')
        if args[0] == 'ping':
            subprocess.call(args)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}