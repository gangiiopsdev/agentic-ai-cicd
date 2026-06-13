from fastapi import FastAPI
import subprocess
import re
class Sanitizer:
    def sanitize(self, host: str):
        return re.sub(r'[^a-zA-Z0-9.-_]', '', host)

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