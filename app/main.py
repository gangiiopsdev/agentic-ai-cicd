from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_\/'
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ["ping", sanitized_host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

# Add input validation for host parameter
def validate_host(host: str):
    # Implement custom validation logic here
    if not re.match(r'^[a-zA-Z0-9.-_\/]+$', host):
        raise ValueError("Invalid host")