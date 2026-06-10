from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.isalnum() and '.' in host:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid host input')

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'result': safe_ping(host)}