from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    if not isinstance(host, str) or ' ' in host:
        raise ValueError('Invalid host name')
    try:
        command = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}