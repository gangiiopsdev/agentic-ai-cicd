from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_input(host):
    if '||' in host or ';' in host or '&' in host or '`' in host or '$(' in host or ')':
        raise ValueError("Invalid input")

@app.get("/ping")
def ping(host: str):
    validate_input(host)
    command_parts = ['ping', host]
    output = execute_command(command_parts)
    return {'status': 'completed', 'output': output}