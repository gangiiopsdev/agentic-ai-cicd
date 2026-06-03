from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in input_string if c in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    # Sanitize the host input to prevent command injection\n    sanitized_host = sanitize_input(host)\n    args = ['ping', sanitized_host]\n    subprocess.run(args, check=True)\n    return {"status": "completed"}