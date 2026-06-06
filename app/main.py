from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in input_string:
        if char not in allowed_chars:
            return False
    return True

def secure_ping(host: str):
    try:
        result = subprocess.run(shlex.split('ping ' + host), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr}, 500

def escape_shell_arg(arg):
    return shlex.quote(arg)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_input(host):
        escaped_host = escape_shell_arg(host)
        return secure_ping(escaped_host)
    else:
        return {"error": "Invalid input"}, 400