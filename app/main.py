from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)