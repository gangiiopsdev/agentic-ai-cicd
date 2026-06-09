from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host and isinstance(host, str) and 'ping' not in host:
        args = ['ping', host]
        subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}

# Preventive controls:
1. Validate input to ensure it does not contain malicious content.
2. Use a whitelist of allowed hosts instead of blacklisting disallowed ones.