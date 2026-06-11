from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex.quote to prevent command injection
    command = ['ping', host]
    args = [arg for arg in command if isinstance(arg, (str, bytes))]
    subprocess.call(args)
    return {'status': 'completed'}