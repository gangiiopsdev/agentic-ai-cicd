from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(value):
    return ''.join(e for e in value if e.isalnum() or e in '.-')

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    # Secure implementation
    subprocess.call(f"ping {host}", shell=False)

    return {"status": "completed"}