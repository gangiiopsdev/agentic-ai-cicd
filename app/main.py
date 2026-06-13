from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize input
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError("Invalid host")
        output = subprocess.check_output(['/usr/bin/ping', shlex.quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}
    except Exception as e:
        return {"status": "failed", "error": str(e)}