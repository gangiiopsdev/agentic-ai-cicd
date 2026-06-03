from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_subprocess(command, args):
    process = subprocess.Popen([command] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

@app.get("/ping")
def ping(host: str):
    # Secure implementation with proper input sanitization and validation
    safe_host = host.replace(';', '').replace('&', '')  # Example of basic input sanitization
    if not all(c.isalnum() for c in safe_host):  # Basic validation
        return {'status': 'error', 'message': 'Invalid input'}
    output, error = safe_subprocess("ping", [safe_host])
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}