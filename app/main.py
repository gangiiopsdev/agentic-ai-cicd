from fastapi import FastAPI
import subprocess
def execute_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.returncode} - {e.stderr}"

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
        return {"status": "invalid input"}
    escaped_host = host.replace(';', '').replace('&', '').replace('|', '').replace('^', '')
    command_parts = ["ping", escaped_host]
    result = execute_safe_command(command_parts)
    return {"status": "completed", "result": result}