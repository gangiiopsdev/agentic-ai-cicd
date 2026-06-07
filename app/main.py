from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_safe_command(command: str):
    subprocess.run(command.split(), check=True)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_command = f"ping {host}"
    run_safe_command(safe_command)

    return {"status": "completed"}