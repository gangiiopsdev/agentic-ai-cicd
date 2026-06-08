from fastapi import FastAPI
import shlex
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in input_str if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = shlex.quote(sanitize_input(host))
    subprocess.run(['ping', '-c', '1', safe_host], check=True, capture_output=True)

    return {"status": "completed"}