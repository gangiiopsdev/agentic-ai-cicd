from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host):
    # Add your validation logic here
    return host.isalnum() and '.' in host
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "error", "error": "Invalid host provided"}
    safe_host = shlex.quote(host)
    command = ['ping', '-c', '1', safe_host]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}