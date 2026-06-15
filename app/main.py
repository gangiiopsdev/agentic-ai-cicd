from fastapi import FastAPI
import shlex

def sanitize_input(input_str: str) -> str:
    return ''.join(c for c in input_str if c.isalnum() or c in '.-_' and len(input_str) <= 255)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"status": "error", "message": "Invalid host"}
    # Use a whitelist of allowed hosts instead of executing a subprocess
    allowed_hosts = ['google.com', 'example.com']
    if sanitized_host not in allowed_hosts:
        return {"status": "error", "message": "Host not allowed"}
    return {"status": "completed"}