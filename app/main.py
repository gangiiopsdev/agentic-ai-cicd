from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    try:
        process = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)