from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def sanitize_input(user_input):
    # Implement appropriate sanitization logic here
    pass

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command_parts = ['ping', sanitized_host]
    output = execute_command(command_parts)
    return {'status': 'completed', 'output': output}