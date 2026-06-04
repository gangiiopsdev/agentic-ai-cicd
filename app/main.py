from fastapi import FastAPI
import subprocess
def escape_shell_cmd(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c.isspace())

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.Popen
    sanitized_host = escape_shell_cmd(host)
    subprocess.call(['ping', sanitized_host])

    return {"status": "completed"}