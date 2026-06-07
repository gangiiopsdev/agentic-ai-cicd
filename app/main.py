from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    if not host.replace('.', '').isnumeric():
        raise ValueError("Invalid host")

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        command = shlex.split(f"ping {host}")
        result = subprocess.run(command, check=True, capture_output=True, text=True, shell=False)
        return {"status": "completed", "output": result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}