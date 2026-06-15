from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host or not host.strip():
        raise ValueError("Invalid host")
    if ' ' in host:
        raise ValueError("Host contains invalid characters")
    return host
def sanitize_input(input_str):
    # Implement input sanitization logic here
    sanitized = ''.join(char for char in input_str if char.isalnum() or char in ['.', '-'])
    return sanitized
class SafePinger:
    def __init__(self, max_ping_count=10):
        self.max_ping_count = max_ping_count
        self.ping_count = 0

    async def ping(self, host: str):
        if self.ping_count >= self.max_ping_count:
            raise ValueError("Too many pings")
        self.ping_count += 1
        validated_host = validate_host(sanitize_input(host))
        output = subprocess.check_output(shlex.split(f'ping -c 1 {validated_host}'), stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
app = FastAPI()
pinger = SafePinger()
@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        result = await pinger.ping(host)
        return result
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": e.output.decode()}
    except Exception as e:
        return {"status": "error", "message": str(e)}