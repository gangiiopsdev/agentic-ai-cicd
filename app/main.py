from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(filter(allowed_chars.__contains__, input_string))

@app.get("/ping")
def ping(host: str):
    sanitized_host = shlex.quote(sanitize_input(host))
    if not all(c.isalnum() or c in '._-' for c in sanitized_host):  # Basic validation
        return {"error": "Invalid host"}

    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {
            "status": "completed",
            "output": result.stdout
        }
    except subprocess.CalledProcessError as e:
        return {
            "error": f"Ping failed: {e.stderr}"
        }