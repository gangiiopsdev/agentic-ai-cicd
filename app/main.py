from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host:
        return False
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode(), result.stderr.decode()

@app.get("/ping")
def ping(host: str):    status, output = safe_ping(host)    if status:
        return {'status': 'completed', 'output': output}
    else:
        return {'error': 'Invalid input'}