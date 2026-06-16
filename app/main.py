from fastapi import FastAPI
import subprocess
def ping_host(host):
    cmd = ['ping', host]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()
@app.get('/ping/{host}')
def read_ping(host: str):
    return ping_host(host)