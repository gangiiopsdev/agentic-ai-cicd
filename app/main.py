from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_/')
    return ''.join(filter(allowed_chars.__contains__, input_string))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using Popen with shell=False and list of arguments
    subprocess.Popen(['ping', '-c', '1', sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}