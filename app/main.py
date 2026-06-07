from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum() or e in ['-', '.', '_', ' ', ':', '/'])
app = FastAPI()
@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(shlex.split(f'ping {shlex.quote(sanitized_host)}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.stderr}