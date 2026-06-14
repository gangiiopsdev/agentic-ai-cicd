from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command, args):
    full_command = [command] + shlex.split(args)
    try:
        result = subprocess.run(full_command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    output = execute_command("ping", host)
    return {"status": "completed", "output": output}