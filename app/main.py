from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Add your sanitization logic here, e.g., using regex or a whitelist of allowed characters
    return ''.join(filter(lambda x: x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-', input_string))

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}