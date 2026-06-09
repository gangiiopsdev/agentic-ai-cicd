from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

def run_command(command, timeout=5):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=timeout)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = ['ping', '-c', '1', sanitized_host]
    output = run_command(command)
    return {"status": "completed", "output": output}