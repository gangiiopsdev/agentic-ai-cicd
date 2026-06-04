from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'

    def validate_host(self, host: str) -> bool:
        return all(char in self.allowed_chars for char in host) and len(host) <= 255

    def run_command(self, command_parts: list) -> dict:
        try:
            result = subprocess.run(command_parts, capture_output=True, text=True, timeout=10)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.TimeoutExpired:
            return {'error': 'Ping request timed out'}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    if safe_ping_instance.validate_host(host):
        command_parts = shlex.split(f'"ping" {host}')
        return safe_ping_instance.run_command(command_parts)
    else:
        return {'error': 'Invalid input'}