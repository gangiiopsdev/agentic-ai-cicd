from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

# Preventive controls
1. Use a whitelist for allowed hostnames/IP addresses instead of sanitizing the input.
2. Avoid using `subprocess.run` with user-provided command arguments when possible.
3. Validate and sanitize the sanitized_host further to ensure it does not contain unexpected characters or patterns.