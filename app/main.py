from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Preventive Controls
# 1. Input Validation: Validate and sanitize the host input to ensure it only contains allowed characters.
# 2. Least Privilege: Run the application with a limited user account that has minimal privileges.
# 3. Security Awareness Training: Ensure developers are aware of common security vulnerabilities and best practices.