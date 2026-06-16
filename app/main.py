from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(host):
    if not host.isalnum() or ' ' in host:
        raise ValueError("Invalid host")
    return shlex.quote(host)

@app.get="/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        args = ['ping', sanitized_host]
        result = subprocess.run(args, capture_output=True, text=True, check=True, shell=False)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}