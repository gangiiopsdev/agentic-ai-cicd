from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['.', '-', '_'])

def safe_subprocess(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host or ' ' in sanitized_host:
        return {'status': 'error', 'output': 'Invalid input'}
    command_parts = ['ping', shlex.quote(sanitized_host)]  # Use shlex.quote for additional security
    result = safe_subprocess(command_parts)
    return {'status': 'completed', 'output': result}