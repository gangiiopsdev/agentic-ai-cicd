from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)
def validate_command(command):
    for word in command:
        if not all(char.isalnum() or char.isspace() for char in word):
            raise ValueError("Invalid characters detected in command")

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = shlex.split(f'ping -c 1 {sanitized_host}')
    try:
        validate_command(command)
        output = subprocess.run(command, capture_output=True, text=True, timeout=5, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except subprocess.TimeoutExpired:
        return {"status": "failed", "error": "Command timed out"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}