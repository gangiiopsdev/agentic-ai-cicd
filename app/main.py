from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    # Implement a more robust function to sanitize and validate user inputs
    return ''.join(c for c in input_str if c.isalnum() or c in ['.', '-', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"status": "failed", "error": "Invalid input"}
    command_parts = ['ping', shlex.quote(sanitized_host)]
    try:
        output = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Additional security measures
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)