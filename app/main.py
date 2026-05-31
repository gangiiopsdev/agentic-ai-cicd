from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(arg):
    return arg.replace('`', '').replace('$', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    host = escape_shell_argument(host)
    # Secure implementation
    subprocess.call(f"ping {host}", shell=False)
    return {"status": "completed"}