from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    # Implement input sanitization logic here
    return ''.join(e for e in user_input if e.isalnum() or e in ('.', ':', '-', '_'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"error": "Invalid input"}
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}