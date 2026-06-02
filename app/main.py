from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ('-', '.', '_', '/'))

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = sanitize_input(host)
    command = ['ping', sanitized_host]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}