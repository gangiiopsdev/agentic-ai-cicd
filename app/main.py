from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    # Implement sanitization logic here
    return ''.join(c for c in user_input if c.isalnum() or c in '.-')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.quote(sanitize_input(host))
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}