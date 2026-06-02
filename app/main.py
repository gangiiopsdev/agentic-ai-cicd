from fastapi import FastAPI
import subprocess
cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum() or '@' in host or ':' in host or '/' in host:
        raise ValueError("Invalid host input")

    # Use a safe way to construct the command with shell=False
    cmd = ['ping', '-c', '1', host]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True, shell=False)
    return {"status": "completed", "output": result.stdout}

try:
    app.include_router(ping)
except Exception as e:
    print(e)