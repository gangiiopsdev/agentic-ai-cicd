from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __call__(self, host):
        try:
            cmd = ['ping'] + shlex.split(host)
            output = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return {"status": "completed", "output": output.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid host name"}
    safe_ping_instance = SafePing()
    return safe_ping_instance(host)