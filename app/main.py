from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    escaped_host = ' '.join(shlex.quote(part) for part in host.split())
    subprocess.run(['ping', escaped_host], check=True, shell=False)
    return {"status": "completed"}