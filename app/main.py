from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    sanitized_input = ''.join(char for char in input_str if char in allowed_chars)
    return sanitized_input
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        args = shlex.split(f'ping -c 1 {sanitized_host}')  # Limit the number of pings to prevent DoS
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": args[2].decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}