from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.Popen
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'stdout': output.decode(), 'stderr': error.decode()}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return result