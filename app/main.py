from fastapi import FastAPI
import subprocess
import shlex

async def safe_global_ping(host: str) -> None:
    # Use shlex.quote to safely escape the host parameter
    cmd = ['ping', '-c', '1'] + shlex.split(shlex.quote(host))
    result = await subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_global_ping(host)
    return {"status": "completed"}