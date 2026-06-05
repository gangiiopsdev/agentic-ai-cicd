from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c == '.').strip()

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        # Use a safer method to avoid command injection
        result = subprocess.run([quote('ping'), quote('-c'), '1', quote(sanitized_host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "message": "Ping successful", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}