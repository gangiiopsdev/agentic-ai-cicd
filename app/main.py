from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host):
    try:
        result = await subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e.stderr)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    is_safe, output = await safe_ping(host)
    if is_safe:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": output}