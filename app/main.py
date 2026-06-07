from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not all(c.isalnum() or c in '.-/' for c in host):
        raise ValueError("Invalid hostname")
    # Use subprocess.run instead of subprocess.Popen for better security
    result = subprocess.run(['ping', shlex.quote(host)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return {"status": "completed", "output": result.stdout, "error": result.stderr if result.stderr else None}