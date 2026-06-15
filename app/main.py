from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Simple validation example - allow only alphanumeric characters and hyphens
    return host.isalnum() or '-' in host

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid host"}, 400
    command = f"ping {shlex.quote(host)}"
    args = shlex.split(command)
    subprocess.run(args, check=True, shell=False)  # Added shell=False to prevent shell injection
    return {"status": "completed"}