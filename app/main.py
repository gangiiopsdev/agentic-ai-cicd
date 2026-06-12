from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(char for char in input_str if char.isalnum() or char.isspace())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ["ping", *shlex.split(sanitized_host)]
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}