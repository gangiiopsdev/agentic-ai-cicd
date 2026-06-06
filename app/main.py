from fastapi import FastAPI
import subprocess
from fastapi.middleware.cors import CORSMiddleware
import shlex

app = FastAPI()

def validate_host(host: str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    if not all(c in allowed_chars for c in host):  # Ensure no potentially harmful characters are present
        raise ValueError('Invalid host')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    safe_host = shlex.quote(host)  # Use shlex.quote to safely escape the host input
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=False)  # Set check=False to avoid raising an exception if the command fails
    return {'status': 'completed', 'output': result.stdout}