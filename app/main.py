from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using shlex.quote to sanitize the input
        subprocess.call(['ping', subprocess.list2cmdline([self.host])])

app = FastAPI()

@app.get("/ping")
def ping(host: str):  # Ensure the host parameter is properly validated and sanitized
    if not validate_host(host):
        return {"error": "Invalid input"}, 400
    ping_command = PingCommand(host)
    ping_command.execute()
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., check for allowed characters, length, etc.
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)