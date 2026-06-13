from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_user_input(host):
    return ''.join(c if c.isalnum() or c in ['.', '-'] else '_' for c in host)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_user_input(host)
    subprocess.call(f"ping {escaped_host}", shell=True)

    return {"status": "completed"}