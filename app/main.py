from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        response = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
        return response.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}