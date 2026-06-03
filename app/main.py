from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command):
    args = shlex.split(command)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_input(input):
    if 'ping' not in input or '--help' in input or '-h' in input:
        raise ValueError("Invalid command")

@app.get("/ping")
def ping(host: str):
    try:
        validate_input(host)
        command = f"ping {host}"
        output = run_command(command)
        return {"status": "completed", "output": output}
    except ValueError as e:
        return {"status": "error", "message": str(e)}