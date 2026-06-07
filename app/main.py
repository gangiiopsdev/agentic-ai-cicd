from fastapi import FastAPI
import subprocess
import shlex

global host_pattern
host_pattern = re.compile(r'^([a-zA-Z0-9.-]+)$')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host_pattern.match(host):
        return {"status": "error", "message": "Invalid host name"}
    # Secure implementation using subprocess.run
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}