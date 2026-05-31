from fastapi import FastAPI
import subprocess
def sanitize_host(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

class SafePingCommand:
    @staticmethod
def safe_ping(host: str) -> list:
        allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
        if host not in allowed_hosts:
            raise ValueError("Host is not allowed")
        return ["ping", host]

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host.strip():
        return {"error": "Host parameter is empty or invalid"}
    try:
        args = SafePingCommand.safe_ping(sanitized_host)
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}