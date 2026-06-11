from fastapi import FastAPI
import subprocess
import shlex
import re
class Sanitizer:
    @staticmethod
def sanitize_input(input_string):
        # Using shlex.quote for better sanitization
        return shlex.quote(input_string)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = Sanitizer.sanitize_input(host)
    # Ensure the host is a valid IP address or domain name before passing to subprocess
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        return {"error": "Invalid host"}, 400
    # Use a safer method like subprocess.run with a list of arguments to avoid shell injection
    subprocess.run(['ping', '-c', '1', sanitized_host], check=True, capture_output=True)
    return {"status": "completed"}