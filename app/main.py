from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_command(command: str) -> str:
    return ' '.join(subprocess.list2cmdline(arg.split()) for arg in command)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(escape_shell_command(["ping", host]), shell=False)
    return {"status": "completed"}