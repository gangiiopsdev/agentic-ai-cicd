from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    host = escape_shell_argument(host)
    # Safer implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}