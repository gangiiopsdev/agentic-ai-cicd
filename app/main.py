from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_string))

@app.get("/ping")
def ping(host: str):
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        return {"error": "Invalid input"}
    sanitized_host = sanitize_input(host)
    try:
        subprocess.run(['ping', '-c', '1', sanitized_host], check=True)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    return {"status": "completed"}