from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    @staticmethod
def ping(host: str):
        if not host:
            raise ValueError("Host cannot be empty")
        # Use a whitelist of allowed hosts to prevent command injection
        allowed_hosts = ['google.com', 'bing.com']  # Example whitelist
        if host not in allowed_hosts:
            raise ValueError("Host is not allowed")
        # Sanitize the input by escaping special characters before using it in the command
        sanitized_host = shlex.quote(host)
        command = ["ping", sanitized_host]
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e.stderr)
app = FastAPI()
@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping_endpoint(host: str):
    result = PingService.ping(host)
    return {"status": "completed", "result": result}