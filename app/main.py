from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return {'status': 'completed', 'output': run_ping(host)}