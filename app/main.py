from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run
    sanitized_host = host.strip()
    if all(c.isalnum() or c in '-.' for c in sanitized_host):
        subprocess.run(['ping', sanitized_host], check=True)