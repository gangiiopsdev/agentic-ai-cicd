from fastapi import FastAPI
import subprocess
class CommandSanitizer:
    @staticmethod
def sanitize_command(command: str) -> list:
        return [arg for arg in command.split() if not any(char in arg for char in '|&;`$*?{}[]\<>"')]
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = CommandSanitizer.sanitize_command(host)
    subprocess.call(['ping'] + sanitized_host)
    return {"status": "completed"}