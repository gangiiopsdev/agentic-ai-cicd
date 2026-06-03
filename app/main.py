from fastapi import FastAPI
import subprocess
import shlex
globally_banned_hosts = {'127.0.0.1', '::1'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    if host in globally_banned_hosts:
        raise ValueError('Host is not allowed')

    try:
        args = shlex.split(f'ping -c 1 {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except Exception as e:
        return {"status": "failed", "error": str(e)}