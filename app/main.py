from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = result.communicate()
        return {'status': 'completed', 'output': output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)