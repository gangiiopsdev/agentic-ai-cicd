from fastapi import FastAPI
import subprocess

app = FastAPI()

def get_safe_command(host):
    if not host.isdigit():
        return None
    return ['ping', host]

@app.get("/ping")
def ping(host: str):
    command = get_safe_command(host)
    if command:
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        return {
            "status": "completed",
            "output": result.stdout,
            "stderr": result.stderr
        }
    else:
        return {"status": "invalid host"}