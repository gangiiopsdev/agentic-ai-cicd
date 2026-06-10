from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    # Simple validation to avoid injection
    if not all(c.isalnum() for c in input_str) and input_str != 'localhost':
        raise ValueError('Invalid input')
@app.get("/ping")
def ping(host: str):
    try:
        sanitize_input(host)
        args = shlex.split(f"ping {host}")
        subprocess.run(args, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    except ValueError as e:
        return {'error': str(e)}
    return {'status': 'completed'}