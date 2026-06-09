from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

def sanitize_host(host):
    # Basic sanitization to prevent injection of malicious commands
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

def safe_subprocess_call(command_parts):
    # Use shlex.quote to safely escape command arguments
    quoted_command_parts = [shlex.quote(part) for part in command_parts]
    subprocess.call(quoted_command_parts)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    # Secure implementation
    safe_subprocess_call(['ping', sanitized_host])
    return {'status': 'completed'}