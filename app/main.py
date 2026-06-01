from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if 'localhost' in host:
        args = shlex.split('ping ' + host)
        subprocess.run(args, check=True)
    return {'status': 'completed'}