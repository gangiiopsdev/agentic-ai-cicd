from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', '-c', '1', host]
    subprocess.call(args)
    return {'status': 'completed'}