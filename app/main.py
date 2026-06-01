from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_command(command: str) -> str:
    return ' '.join(subprocess.list2cmdline([arg.strip() for arg in command.split()]))

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(escape_shell_command(f"ping {host}"))
    return {"status": "completed"}