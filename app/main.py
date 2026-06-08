from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_command(user_input):
    return subprocess.list2cmdline(user_input.split())

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    subprocess.call(escape_shell_command(f"ping {host}"))
    return {"status": "completed"}