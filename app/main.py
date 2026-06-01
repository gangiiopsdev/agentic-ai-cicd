from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return input_str.strip()

def execute_safe_command(command):
    if all(isinstance(arg, str) for arg in command):
        subprocess.run(command, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', sanitized_host]
    execute_safe_command(command)
    return {"status": "completed"}