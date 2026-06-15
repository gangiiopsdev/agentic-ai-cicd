from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@app.get("/ping")
def ping(host: str):
    command_parts = ['ping', host]
    status = execute_safe_command(command_parts)
    return {'status': 'completed', 'result': status}