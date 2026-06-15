from fastapi import FastAPI
import subprocess
import shlex

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_string if char in allowed_chars)

def execute_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not validate_host(sanitized_host):
        return {"status": "failed", "error": "Invalid host"}
    command_parts = ['ping', shlex.quote(sanitized_host)]
    output = execute_command(command_parts)
    if isinstance(output, Exception):
        return {"status": "failed", "error": str(output)}
    else:
        return {"status": "completed", "output": output}

# Additional preventive controls:
# - Use a whitelist of allowed hosts
# - Log all executed commands and their outputs for auditing


# Validate the host against a whitelist
def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts