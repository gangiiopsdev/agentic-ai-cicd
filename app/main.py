from fastapi import FastAPI
import subprocess
def sanitize_input(input_str: str) -> str:
    return ''.join(e for e in input_str if e.isalnum() and e.isprintable())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host or len(sanitized_host) > 255:
        return {'status': 'error', 'message': 'Invalid host'}

    args = ['ping', '-c', str(len(sanitized_host)), sanitized_host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)

    return {'status': 'completed', 'output': result.stdout}