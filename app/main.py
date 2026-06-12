from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    # Safe implementation using a list instead of a shell command
    subprocess.call(['ping', host])
    return {"status": "completed"}