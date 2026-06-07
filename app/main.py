from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=10)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

# Preventive Controls:
# 1. Validate and sanitize input to ensure it does not contain malicious content.
# 2. Use a whitelist of allowed hosts or implement IP whitelisting.
# 3. Consider using parameterized queries if applicable.