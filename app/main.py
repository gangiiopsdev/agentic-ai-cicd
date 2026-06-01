from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def ping(host: str):
        # Safer implementation with argument parsing to avoid shell injection
        try:
            cmd = ['ping', host]
            args = shlex.split(' '.join(cmd))
            output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
            return {"status": "completed", "output": output}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.output}

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    # Sanitize input to prevent shell injection
    if not all(c.isalnum() or c in '-.' for c in host):
        return {"status": "failed", "error": "Invalid characters in host name"}
    return SafePing.ping(host)