from fastapi import FastAPI
import subprocess
import shlex

class PingException(Exception):
    pass

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Secure implementation using shlex.split to avoid shell injection
        subprocess.call(shlex.split(f'ping {shlex.quote(host)}'))
        return {'status': 'completed'}
    except Exception as e:
        raise PingException(str(e))