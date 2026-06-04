from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def execute_command(command_parts):
    try:
        result = subprocess.run([quote(part) for part in command_parts], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    command_parts = ['ping', quote(host)]
    output = execute_command(command_parts)
    return {'status': 'completed', 'output': output}