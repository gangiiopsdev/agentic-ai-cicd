from fastapi import FastAPI
import subprocess

generate_command = lambda host: ['ping', '-c', '4', host]

app = FastAPI()

def sanitize_host(host: str) -> str:
    return ''.join(char for char in host if char.isalnum() or char in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not is_valid_host(sanitized_host):
        raise ValueError("Invalid host")
    subprocess.run(generate_command(sanitized_host), check=True)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Basic validation to ensure the input does not contain any malicious characters
    return all(char.isalnum() or char in ('.', '-', '_') for char in host)