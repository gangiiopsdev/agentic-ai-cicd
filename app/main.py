from fastapi import FastAPI
import subprocess

def ping(host: str):
    if not host.replace('.', '', 3).isdigit():
        return {'status': 'error', 'output': 'Invalid host'}
    safe_host = host.split()[0]  # Sanitize input to prevent command injection
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}