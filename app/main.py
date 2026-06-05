from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using shlex.quote to escape the input
    from shlex import quote
    subprocess.call(f"ping {quote(host)}")

@app.get("/ping")
def ping_handler(host: str):
    result = ping(host)
    return {'status': 'completed'}