from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)
def sanitize_command(command):
    allowed_commands = ['ping']  # Define a whitelist of allowed commands
    return command if command in allowed_commands else None
class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        subprocess.run([command] + list(args), check=True)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    sanitized_command = sanitize_command('ping')
    if sanitized_host and sanitized_command:
        SafeSubprocess.run(sanitized_command, sanitized_host)
    return {'status': 'completed'}