from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output.strip()}'

def ping(host: str):
    # Safer implementation
    result = safe_ping(subprocess.quote(host))  # Use subprocess.quote to escape user input
    return {'status': 'completed', 'output': result}