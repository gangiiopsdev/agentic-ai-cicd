from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE

app = FastAPI()

def safe_ping(host):
    try:
        process = Popen(['ping', host], stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if process.returncode != 0:
            raise Exception(f'Error pinging {host}: {error.decode()}')
        return output.decode().strip()
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)