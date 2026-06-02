from fastapi import FastAPI
import subprocess
global ALLOWED_HOSTS = {'host1', 'host2'}

app = FastAPI()

def safe_ping(host):
    if host not in ALLOWED_HOSTS:
        raise ValueError('Host is not allowed')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return {"status": "completed", "output": response}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}