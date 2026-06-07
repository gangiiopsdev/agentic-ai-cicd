from fastapi import FastAPI
import subprocess
app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in input_string if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.Popen with input validation and sanitization
    sanitized_host = sanitize_input(host)
    if len(sanitized_host) > 255:
        return {"status": "error", "message": "Invalid hostname length"}
    try:
        process = subprocess.Popen(['ping', sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}
    except Exception as e:
        return {"status": "error", "message": str(e)}