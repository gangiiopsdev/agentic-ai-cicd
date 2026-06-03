from fastapi import FastAPI
import subprocess
from typing import Union
def is_valid_host(host: str) -> bool:
    # Simple validation, replace with more robust logic if needed
    return host.replace('.', '').isalnum()

app = FastAPI()

def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', f'-c 1 {host}']  # Limit the number of packets to 1 for security
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}