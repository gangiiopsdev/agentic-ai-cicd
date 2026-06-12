from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    safe_host = shlex.quote(host)
    subprocess.call(['ping', '-c', '1', safe_host])  # Use -c to limit the number of pings
    return {'status': 'completed'}