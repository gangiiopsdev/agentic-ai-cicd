from fastapi import FastAPI
import subprocess
def escape_shell_cmd(cmd):
    return ' '.join([subprocess.quote(arg) for arg in cmd.split()])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(escape_shell_cmd(f'ping {host}'))
    return {"status": "completed"}