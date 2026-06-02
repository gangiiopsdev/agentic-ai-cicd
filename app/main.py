from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_command(cmd_parts):
    return ' '.join(shlex.quote(part) for part in cmd_parts)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(safe_command(['ping', host]).split())
    return {"status": "completed"}