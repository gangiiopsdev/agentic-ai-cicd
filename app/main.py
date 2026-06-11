from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.Popen
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

@app.get("/ping")
def ping(host: str):,
    output, error = safe_ping(host)
    if error:
        return {'status': 'error', 'message': error.decode()}
    return {'status': 'completed', 'output': output.decode()}