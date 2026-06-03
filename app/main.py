from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    if not input_str:
        return None
    safe_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(char for char in input_str if char in safe_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"status": "error", "message": "Invalid host parameter"}
    result = subprocess.run(['ping', '-c 1', shlex.quote(sanitized_host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}