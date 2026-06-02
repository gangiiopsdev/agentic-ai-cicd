from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum():
        return {'status': 'invalid_input'}
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}