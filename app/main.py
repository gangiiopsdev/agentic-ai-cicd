from fastapi import FastAPI
import subprocess
def sanitize_input(value):
    # Implement input sanitization logic here
    return value.strip()
app = FastAPI()
def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ["ping", sanitized_host]
    output = execute_command(command)
    return {"status": "completed", "output": output}