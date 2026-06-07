from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using a safe method
    subprocess.run(['ping', host], shell=False, check=True)
    return {'status': 'completed'}