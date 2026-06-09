from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    def __init__(self):
        self.cmds = {'ping': self.ping}

    def ping(self, host):
        args = shlex.split(f'ping {host}')
        subprocess.run(args)

app = FastAPI()
safe_subprocess = SafeSubprocess()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in safe_subprocess.cmds:
        safe_subprocess.cmds[host](host)
    else:
        raise HTTPException(status_code=403, detail="Invalid command")
    return {"status": "completed"}