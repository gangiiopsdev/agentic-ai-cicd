from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

def sanitize_command(command):
    allowed_commands = ['ping']  # Define a whitelist of allowed commands
    return command if command in allowed_commands else None

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    sanitized_command = sanitize_command('ping')
    if sanitized_host and sanitized_command:
        subprocess.run([sanitized_command, sanitized_host], check=True)
    return {'status': 'completed'}