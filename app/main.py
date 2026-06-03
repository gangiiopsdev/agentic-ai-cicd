from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in input_str if c in allowed_chars)

def safe_subprocess_call(command_parts):
    try:
        subprocess.run(command_parts, check=True, shell=False)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Subprocess call failed: {e}")
        return False

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command_parts = ['ping', shlex.quote(sanitized_host)]
    if safe_subprocess_call(command_parts):
        return {"status": "completed", "result": "success"}
    else:
        return {"status": "completed", "result": "failure"}