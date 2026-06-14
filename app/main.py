from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(allowed_chars.__contains__, input_string))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    sanitized_host = sanitize_input(host)
    if not sanitized_host or '--' in sanitized_host:
        raise ValueError("Invalid host input")
    subprocess.run(['ping', f'{sanitized_host}'], check=True, shell=False)
    return {"status": "completed"}