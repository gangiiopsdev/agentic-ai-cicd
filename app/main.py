from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and arguments tuple
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}