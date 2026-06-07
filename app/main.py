from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_input(host):
        raise ValueError("Invalid input")
    return {"status": safe_ping(host)}

def validate_input(input_str: str) -> bool:
    # Add validation logic here to ensure the input is safe
    return input_str.isalnum()