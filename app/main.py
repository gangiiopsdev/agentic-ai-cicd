from fastapi import FastAPI
import subprocess
def execute_safe_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host):
        raise ValueError("Invalid host parameter")
    command = ["ping", host]
    output = execute_safe_command(command)
    return {"status": "completed", "output": output}