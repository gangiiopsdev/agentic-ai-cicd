from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

def safe_ping(host: str):
    if '&&' in host or ';' in host or '|' in host:
        raise HTTPException(status_code=400, detail='Invalid input')
    try:
        args = ['ping', host]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr.decode('utf-8')}"

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)