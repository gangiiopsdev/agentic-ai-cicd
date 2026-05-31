from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_secure_command(command_parts):
    command = ' '.join(shlex.quote(part) for part in command_parts)
    subprocess.run(command, shell=False, check=True)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    run_secure_command(['ping', host])
    return {"status": "completed"}