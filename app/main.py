from fastapi import FastAPI
import subprocess
import shlex
class Sanitizer:
    def sanitize(self, host: str):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
        return ''.join(char for char in host if char in allowed_chars)

app = FastAPI()

async def safe_ping(host: str):
    # Use shlex to safely handle the command arguments
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent code injection
    sanitizer = Sanitizer()
    sanitized_host = sanitizer.sanitize(host)
    return safe_ping(sanitized_host)