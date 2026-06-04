from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isspace())
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(shlex.split(f"ping {shlex.quote(sanitized_host)}"), check=True, capture_output=True, text=True, timeout=5)
        return {
            "status": "completed",
            "output": result.stdout
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": str(e)
        }