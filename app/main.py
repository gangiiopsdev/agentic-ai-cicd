from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize user input for the 'host' parameter.
    if not host or ' ' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

# Preventive controls:
# 1. Validate and sanitize user input for the 'host' parameter.
# 2. Use a whitelist of allowed hosts or use a more secure alternative to ping (e.g., DNS lookup).
# 3. Consider using environment variables for sensitive configurations.