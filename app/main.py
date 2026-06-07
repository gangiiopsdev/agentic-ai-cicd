from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    # Simple escaping for demonstration purposes; consider using a library for more robust escaping.
    return ''.join(c if c.isalnum() or c in ('.', '-') else '_' for c in host)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(f"ping {escaped_host}", shell=True)
    return {"status": "completed"}