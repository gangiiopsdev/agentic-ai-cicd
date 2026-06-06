from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}

    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

# Preventive Controls
# 1. Validate and sanitize the input to ensure it does not contain malicious characters.
# 2. Use parameterized commands where possible.
# 3. Run the command in a restricted environment with limited privileges.