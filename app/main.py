from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_safe_command(command: str):
    args = shlex.split(command)
    subprocess.run(args, check=True, shell=False)

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    try:
        execute_safe_command(command)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

    return {'status': 'completed'}