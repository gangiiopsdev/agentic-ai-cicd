from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.Popen instead of subprocess.call with shell=True
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'output': output.decode(), 'error': error.decode() if error else None}

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)