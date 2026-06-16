from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c.isdigit())
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        raise ValueError("Invalid host name")
    args = ['ping', subprocess.list2cmdline([sanitized_host])]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}