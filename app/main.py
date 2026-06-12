from fastapi import FastAPI
import subprocess
import shlex

global args = ['ping', '127.0.0.1']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    safe_host = shlex.quote(host)
    args = ['ping', safe_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}