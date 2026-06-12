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
    if not all(c.isdigit() for c in host):  # Ensure the input contains only digits
        return {"status": "error", "message": "Invalid input"}
    if not all(ord(c) < 128 and (c.isalnum() or c.isdigit() or c in ('.', '-', '_')) for c in host):  # Ensure ASCII characters
        return {"status": "error", "message": "Invalid input"}
    ping_command(host)
    return {"status": "completed"}