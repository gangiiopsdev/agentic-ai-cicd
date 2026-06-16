from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Basic sanitization, more robust methods should be used in production
    return ''.join(e for e in input_str if e.isalnum())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    # Secure implementation with additional checks and escaping
    command = ['ping', subprocess.list2cmdline([host])]
    subprocess.run(command, check=True)
    return {"status": "completed"}