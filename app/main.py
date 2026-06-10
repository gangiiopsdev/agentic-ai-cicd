from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host):
    try:
        # Validate and sanitize input
        if not host.strip():
            raise ValueError("Host is empty")
        args = shlex.split(f'ping {shlex.quote(host)}')
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), True
    except Exception as e:
        print(str(e))
        return str(e), False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output, success = safe_ping(host)
    if success:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "message": "Host is empty or invalid", "error": output}