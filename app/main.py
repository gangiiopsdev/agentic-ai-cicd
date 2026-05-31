from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/" )
def home():
    return {"message": "Agentic Self-Healing Pipeline" }

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum() or ' ' in host:
        return {"status": "failed", "error": "Invalid input"}
    args = shlex.split('ping ' + host)
    output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
    return {"status": "completed", "output": output}