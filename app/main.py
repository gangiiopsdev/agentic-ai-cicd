from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        args = ['ping', host]
        result = subprocess.run(shlex.split(' '.join(args)), timeout=5, capture_output=True, text=True)
        if result.returncode == 0:
            return {'status': 'completed'}
        else:
            return {'status': 'failed', 'error': result.stderr}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}