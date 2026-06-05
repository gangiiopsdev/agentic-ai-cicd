from fastapi import FastAPI
import re
import shlex
import subprocess


def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

def validate_and_sanitize_input(input_str, pattern):
    if re.match(pattern, input_str):
        return shlex.split(input_str)
    raise ValueError('Invalid input')

app = FastAPI()

@app.get("/"
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        args = validate_and_sanitize_input(host, r'^[a-zA-Z0-9.-]+$')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    except ValueError as ve:
        return {"status": "error", "message": str(ve)}