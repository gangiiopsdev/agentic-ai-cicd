from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(value):
    return value.replace(';', '').replace('&', '').replace('|', '')

@app.get="/ping")
def ping(host: str):
    # Secure implementation
    escaped_host = escape_shell_argument(host)
    subprocess.call(['ping', escaped_host])
    return {"status": "completed"}