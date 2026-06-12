from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isdigit() or e in ('.', '-', '_'))

def ping_command(host):
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', '-c', '1', sanitized_host], shell=False)

@app.get("/ping")
def ping(host: str):
    if not all(c in ('0', '1') for c in host):  # Validate that the input contains only valid digits
        return {"status": "error", "message": "Invalid input"}
    try:
        ping_command(host)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}