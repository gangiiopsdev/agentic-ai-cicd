from fastapi import FastAPI
import subprocess
import shlex
from fastapi.responses import JSONResponse

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', '-c', '1'] + [shlex.quote(host)], check=True, stdout=subprocess.PIPE)
        return output.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'error': f'Ping failed: {e}'}, status_code=500)

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        return JSONResponse(content={'error': 'Invalid input'}, status_code=400)
    return safe_ping(shlex.quote(host))