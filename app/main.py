from fastapi import FastAPI
import re

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_str if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Enhanced sanitization using regex to match only valid characters
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    subprocess.run(['ping', f'"{sanitized_host}"'], check=True, shell=False)
    return {"status": "completed"}