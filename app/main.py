from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host: str):
    return ''.join(c if c.isalnum() or c in '-.' else '_' for c in host)

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    subprocess.call(f"ping {escape_host(host)}", shell=False)

    return {"status": "completed"}