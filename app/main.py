from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    return subprocess.call(args)

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}