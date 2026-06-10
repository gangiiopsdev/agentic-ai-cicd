from fastapi import FastAPI
import subprocess
class CommandSanitizer:
    def __init__(self, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
        self.allowed_chars = allowed_chars

    def is_safe(self, command):
        return all(char in self.allowed_chars for char in command)

cmd_sanitizer = CommandSanitizer()

app = FastAPI()

@app.get("/ping")
def ping(host: str):  # Secure implementation
    if not cmd_sanitizer.is_safe(host):
        raise ValueError("Invalid input")
    subprocess.call(["ping", host])
    return {"status": "completed"}