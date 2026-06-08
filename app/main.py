from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f"ping {sanitized_host}")
    try:
        subprocess.run(args, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    return {"status": "completed"}