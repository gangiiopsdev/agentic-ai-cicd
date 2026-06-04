from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command: str, args: list):
    try:
        result = subprocess.run([command] + args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@app.get("/ping")
def ping(host: str):
    command = 'ping'
    args = [host]
    return execute_safe_command(command, args)