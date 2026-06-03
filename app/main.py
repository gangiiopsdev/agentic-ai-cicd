from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')

    def is_valid_input(self, host: str) -> bool:
        return all(char in self.valid_chars for char in host)

    def run_command(self, command_parts: list) -> str:
        try:
            result = subprocess.run(command_parts, capture_output=True, text=True, timeout=5, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()
ping_instance = SafePing()

def safe_ping(host: str):
    if not ping_instance.is_valid_input(host):
        return "Invalid input"
    command_parts = shlex.split('ping ' + host)
    return ping_instance.run_command(command_parts)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)