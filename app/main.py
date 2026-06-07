from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    return ''.join(char for char in user_input if char.isalnum() or char in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    # Sanitize input
    sanitized_host = sanitize_input(host)
    
    # Use subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    
    return {"status": "completed", "output": result.stdout}