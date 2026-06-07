from fastapi import FastAPI
import subprocess
def escape_shell_cmd(cmd):
    return [arg.replace(';', '').replace('&', '') for arg in cmd.split()]

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = escape_shell_cmd(f"ping {host}")
    subprocess.call(args)

    return {"status": "completed"}