from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.isnumeric():
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Invalid input for ping command')

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    result = safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}