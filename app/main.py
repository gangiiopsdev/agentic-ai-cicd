from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ' .-_')

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with sanitized input
    try:
        result = subprocess.run(['ping', sanitize_input(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}