from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    args = ['ping', *shlex.split(host)]
    result = subprocess.run(args, check=True, capture_output=True)
    return result.stdout.decode('utf-8')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Basic validation to ensure the input is alphanumeric
        raise ValueError("Invalid input")
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode('utf-8')}