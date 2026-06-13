from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    args = ['ping', host]
    # Sanitize the host input to prevent OS command injection
    sanitized_host = ''.join(e for e in host if e.isalnum() and not e.isspace())
    args[1] = sanitized_host  # Replace the first argument with the sanitized host
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()
@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get="/ping"
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid host input"}
    response = safe_ping(host)
    return {"status": "completed", "output": response}