from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return ''.join(c if c.isalnum() or c in '._-' else f'\{ord(c):03o}' for c in arg)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}