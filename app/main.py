from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = ''.join(filter(str.isalnum, host))
    args = ['ping', safe_host]
    subprocess.call(args)

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)