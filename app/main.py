from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    # Implement proper sanitization logic here
    return ''.join(c for c in user_input if c.isalnum() or c in ('.', '-', '_'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.quote(sanitize_input(host))
    try:
        subprocess.call(['ping', sanitized_host], shell=False)
    except Exception as e:
        return {"error": str(e)}
    return {"status": "completed"}