from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        args = ['ping', '-c', '1'] + [arg for arg in host.split() if arg.strip()]  # Validate and sanitize input
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}