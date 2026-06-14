from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

def sanitize_input(user_input: str) -> str:
    # Implement input sanitization logic here
    return user_input.strip()

@app.get("/ping")
def ping_endpoint(host: str):
    sanitized_host = sanitize_input(host)
    return ping(sanitized_host)