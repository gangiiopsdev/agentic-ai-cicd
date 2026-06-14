from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    return ''.join(filter(str.isalnum, user_input))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}