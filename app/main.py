from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.returncode} - {e.stderr.strip()}

def ping(host: str):
    # Secure implementation
    output = run_ping(host)
    return {'status': 'completed', 'output': output}