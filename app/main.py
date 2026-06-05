from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return ''.join(c if c.isalnum() else '_' for c in arg)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(f'ping {escape_shell_arg(host)}', shell=True)
    return {"status": "completed"}