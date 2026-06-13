from fastapi import FastAPI
import subprocess
def sanitize_input(input_str: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(allowed_chars.__contains__, input_str))
def ping(host: str):
    sanitized_host = subprocess.quote(sanitize_input(host))  # Use subprocess.quote for safe command construction
    args = ['ping', '-c', '1', sanitized_host]  # Limit ping to one packet for security
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f'Ping failed with error: {result.stderr}')
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)