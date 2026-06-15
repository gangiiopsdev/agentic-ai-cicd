from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def sanitize_host(host):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        return ''.join(char for char in host if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = PingCommand.sanitize_host(host)
    subprocess.call(f"ping {sanitized_host}")
    return {"status": "completed"}