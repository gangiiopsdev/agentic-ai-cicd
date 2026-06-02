from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate host input (e.g., allow only certain domains)
        if not valid_host(host):
            raise ValueError("Invalid host")
        subprocess.call(["ping", host])
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

# Example validation function
import re
def valid_host(host: str) -> bool:
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None