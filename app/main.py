from fastapi import FastAPI
import subprocess
def escape_input(user_input):
    return ''.join(c for c in user_input if c.isalnum() or c in (' ', '.', '-', '/', ':'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    escaped_host = escape_input(host)
    try:
        result = subprocess.run(['ping', escaped_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}