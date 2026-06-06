from fastapi import FastAPI
import subprocess
class HostSanitizer:
    def sanitize(self, host: str) -> str:
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        sanitized_host = ''.join(char for char in host if char in allowed_chars)
        return sanitized_host

app = FastAPI()

def ping(host: str):
    # Sanitize the input host before using it with subprocess.run
    sanitized_host = HostSanitizer().sanitize(host)
    # Secure implementation using subprocess.run with a safe list of arguments
    subprocess.run(['ping', sanitized_host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)