from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        # Validate and sanitize input
        if host.strip() == '':
            raise ValueError("Host is empty")
        args = shlex.split(f'ping {shlex.quote(host)}')
        subprocess.run(args, check=True)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed", "message": "Host is empty or invalid"}