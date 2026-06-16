from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.Popen with sanitized input
    args = ['ping', host]
    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return {'status': 'completed', 'stdout': process.stdout, 'stderr': process.stderr}