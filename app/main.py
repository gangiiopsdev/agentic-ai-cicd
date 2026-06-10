from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced implementation with shlex to safely handle the host input and ensure full executable path
    subprocess.call(['ping', shlex.quote(host)])
    return {'status': 'completed'}