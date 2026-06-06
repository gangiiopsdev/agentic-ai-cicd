from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex.quote to sanitize the input
    args = ['ping', '-c', '1', shlex.quote(host)]
    subprocess.run(args, check=True)
    return {'status': 'completed'}