from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = ["ping", host]
    subprocess.run(args, check=True)

async def is_safe_host(host: str) -> bool:
    # Implement a whitelist of allowed hosts or use network policies
    return True

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise HTTPException(status_code=403, detail="Invalid host")
    safe_ping(host)
    return {"status": "completed"}