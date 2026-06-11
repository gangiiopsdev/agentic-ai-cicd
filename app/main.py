from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Use shlex to safely handle the command
        args = shlex.split(f'ping {host}')
        if len(args) > 2 or 'ping' not in args[0]:
            return {'error': 'Invalid host format', 'status': 'failed'}
        subprocess.call(args, shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}