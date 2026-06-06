from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    result = subprocess.call(args)
    return result

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    status = safe_ping(host)

    return {'status': 'completed', 'exit_code': status}