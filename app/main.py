from fastapi import FastAPI
import subprocess
def sanitize_input(input):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in input if c in allowed_chars)

app = FastAPI()
def execute_command(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    cmd = ["ping", sanitized_host]
    result = execute_command(cmd)
    return {"status": "completed", "output": result}