from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def safe_ping(host):
    try:
        cmd = ['ping', host]
        response = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return response.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid hostname")
    return {'status': safe_ping(host)}