from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    if validate_input(host):
        return ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid input'}

def validate_input(input_string: str) -> bool:
    # Implement a function to validate user input
    # For example, check for malicious patterns or length limits
    return input_string.isalnum() and len(input_string) <= 255