from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}

def is_valid_host(host: str) -> bool:
    # Add validation logic here, e.g., check for allowed hosts
    return True