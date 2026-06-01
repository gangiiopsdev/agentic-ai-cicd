from fastapi import FastAPI
import subprocess
def ping(host: str):
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)