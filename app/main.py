from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    sanitized_host = ''.join(filter(str.isalnum, host))
    subprocess.call(['ping', sanitized_host], shell=False)
    return {'status': 'completed'}