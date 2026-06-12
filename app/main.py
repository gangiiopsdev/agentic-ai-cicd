from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

def sanitize_input(input_str):
    # Add your sanitization logic here, e.g., whitelist of allowed characters
    return ''.join(c for c in input_str if c.isalnum() or c.isspace())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command_parts = ['ping', shlex.quote(sanitized_host)]  # Use shlex.quote to ensure safe quoting
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}