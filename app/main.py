from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        return {'status': 'completed', 'output': safe_ping(host)}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}