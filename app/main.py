from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    # Simple validation to avoid injection
    if not all(c.isalnum() for c in input_str) and input_str != 'localhost':
        raise ValueError('Invalid input')
@app.get("/ping")
def ping(host: str):\n    try:\n        sanitize_input(host)
        subprocess.call(shlex.split(f"ping {host}"), shell=False)\n    except ValueError as e:\n        return {'error': str(e)}\n    return {'status': 'completed'}