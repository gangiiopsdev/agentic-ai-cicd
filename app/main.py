from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'  # Add any additional characters as needed
    sanitized = ''.join(char for char in input_str if char in allowed_chars)
    return subprocess.list2cmdline([arg.replace(';', '').replace('&', '').replace('\', '').replace('/', '') for arg in sanitized.split()])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(sanitize_input(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode('utf-8')}