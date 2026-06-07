from fastapi import FastAPI
import subprocess
import shlex
class SanitizedShellInput:
    def __new__(cls, value):
        # Simple sanitization: only allow alphanumeric characters and a few common delimiters
        return ''.join(c for c in value if c.isalnum() or c in ' .-')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input sanitization
    if not host:
        return {"status": "error", "message": "Host parameter is required"}
    sanitized_host = SanitizedShellInput(host)
    command = ["ping", shlex.quote(sanitized_host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}