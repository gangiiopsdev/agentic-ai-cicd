from fastapi import FastAPI
import subprocess

generate_ping_command = lambda host: ['ping', '-c', '4', host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum() or len(host) > 32:
        raise ValueError("Invalid host name")
    # Sanitize the input by escaping special characters
    sanitized_host = subprocess.shlex_quote(host)
    result = subprocess.run(generate_ping_command(sanitized_host), capture_output=True, text=True)
    return {"status": result.stdout}