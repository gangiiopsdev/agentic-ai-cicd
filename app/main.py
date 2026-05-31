from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_input(host):
        return safe_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid input'}
def validate_input(input_str):
    # Implement proper validation logic here, e.g., regex match against allowed characters
    return input_str.isalnum()