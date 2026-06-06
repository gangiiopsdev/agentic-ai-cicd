from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate input to ensure it does not contain malicious characters or patterns
    if any(char in host for char in '"`|&*;()$#@^<>?[]{}\\'):  # Example of a simple validation, more complex logic may be needed based on use case
        raise ValueError("Invalid host")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return {'status': 'completed', 'response': response}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}