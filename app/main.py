from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(value):
    return ''.join(c for c in value if c.isalnum() or c in '-._')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host to prevent command injection
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', '-c', '1'] + shlex.split(shlex.quote(sanitized_host)), check=True, capture_output=True, text=True)
    return {"status": "completed", "response": result.stdout}