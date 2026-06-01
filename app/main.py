from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_/'
    return ''.join(char for char in input_str if char in allowed_chars)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ["ping", sanitized_host]
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": subprocess.getoutput(f'ping {sanitized_host}')}