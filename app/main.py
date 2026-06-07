from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode(), result.stderr.decode()

@app.get("/ping")
def ping(host: str):
    output, error = safe_ping(host)
    if error:
        return {'status': 'error', 'output': error}
    else:
        return {'status': 'completed', 'output': output}