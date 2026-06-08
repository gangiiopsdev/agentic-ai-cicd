from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in input_string if char in allowed_chars)

def escape_shell_arg(arg):
    return shlex.quote(arg)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    escaped_host = escape_shell_arg(sanitized_host)
    try:
        result = subprocess.run(['ping', '-c 4', escaped_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}