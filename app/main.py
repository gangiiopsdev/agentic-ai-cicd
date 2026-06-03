from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output([shell_quote('ping'), shell_quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode("utf-8")}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.output.decode("utf-8")}