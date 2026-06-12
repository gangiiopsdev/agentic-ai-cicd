from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['-', '.', ':', '@'])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Use a whitelist of allowed hosts
    allowed_hosts = ["example.com", "test.com"]
    if sanitized_host not in allowed_hosts:
        return {"status": "error", "message": "Host not allowed"}
    command = ["ping", *shlex.split(sanitized_host)]
    result = subprocess.run(command, check=True, capture_output=True, text=True, shell=False)
    # Ensure the output is sanitized before returning
    return {"status": "completed", "output": ''.join(e for e in result.stdout if e.isprintable())}