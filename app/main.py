from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(value):
    if isinstance(value, str):
        return value.replace(';', '').replace('&', '').replace('\', '\\').replace('$', '\$').replace('^', '\^')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_argument(host)
    subprocess.call(f"ping {escaped_host}", shell=True)

    return {"status": "completed"}