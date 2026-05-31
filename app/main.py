from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', shlex.quote(host)])
    return {'status': 'completed'}