from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using subprocess.Popen for a safer alternative
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'output': output.decode(), 'error': error.decode() if error else None}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)