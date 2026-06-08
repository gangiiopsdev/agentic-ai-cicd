from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host: str):
    return ''.join(c if c.isalnum() or c in '.-_' else '_' for c in host)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    # Secure implementation
    subprocess.call(['ping', escaped_host])

    return {"status": "completed"}