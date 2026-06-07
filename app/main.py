from fastapi import FastAPI
import subprocess
import re
def shell_safe(s):
    return ''.join(c for c in s if c.isalnum() or c in '-._~/+:@&=;?#,$#	\x20')

app = FastAPI()

@app.get("/ping")
def ping(host: str): # Validate the input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid hostname"}
    try:
        result = subprocess.run(["ping", shell_safe(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}