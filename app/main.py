from fastapi import FastAPI
import subprocess
def sanitize_input(input_str: str) -> str:
    return ''.join(e for e in input_str if e.isalnum())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'status': 'error', 'message': 'Invalid host'}

    args = ['ping', sanitized_host]
    subprocess.run(args, check=True, capture_output=True, text=True)

    return {'status': 'completed'}