from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    return ''.join(filter(str.isalnum, user_input))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation with shell=False
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}