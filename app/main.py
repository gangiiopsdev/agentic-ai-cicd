from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isdigit():
        return 'Invalid input'
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get('/ping')
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}