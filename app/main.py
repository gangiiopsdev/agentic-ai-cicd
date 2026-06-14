from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(c if c.isalnum() else '_' for c in host)

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    escaped_host = escape_host(host)
    subprocess.call(f"ping {escaped_host}")

    return {"status": "completed"}