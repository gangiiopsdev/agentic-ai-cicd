from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Using subprocess.run for a safer alternative with shell=False
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
    return {'output': result.stdout, 'error': result.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)