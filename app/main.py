from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        # Validate and sanitize input
        if host.strip() == '':
            raise ValueError("Host is empty")
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.returncode == 0
    except Exception as e:
        print(str(e))
        return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed", "message": "Host is empty or invalid"}