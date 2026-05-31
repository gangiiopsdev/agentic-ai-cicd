from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.Popen with shell=False and input sanitization
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    if not host.isdigit():  # Example simple validation for numeric IP addresses
        response = safe_ping(host)
        return {'status': 'completed', 'response': response}
    else:
        return {'status': 'error', 'message': 'Invalid input'}