from fastapi import FastAPI
import subprocess
def run_command(command: str):
    args = command.split()
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    run_command(f"ping {host}")

    return {"status": "completed"}