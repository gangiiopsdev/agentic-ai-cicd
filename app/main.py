from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if '-' not in host:
        try:
            # Use shlex to safely split the command into arguments
            args = shlex.split('ping ' + host)
            subprocess.call(args, shell=False)
        except Exception as e:
            return {'error': str(e)}
    else:
        raise ValueError('Invalid host parameter')
    return {'status': 'completed'}