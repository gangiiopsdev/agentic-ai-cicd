from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' + chr(9) * 6
    return ''.join(char for char in host if char in allowed_chars)

def validate_host(host):
    valid_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
    return host in valid_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "invalid input"}
    try:
        args = ['ping', f'-c 4 {host}']  # Use validated host directly
        subprocess.run(args, check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}