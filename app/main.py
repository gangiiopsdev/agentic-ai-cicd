from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    try:
        args = ['ping', host]
        subprocess.call(args)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}