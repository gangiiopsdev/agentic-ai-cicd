from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

async def safe_ping(host: str):
    if host not in ALLOWED_HOSTS:
        return "Host is not allowed"
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    status = await safe_ping(host)
    return {"status": "completed", "output": status}