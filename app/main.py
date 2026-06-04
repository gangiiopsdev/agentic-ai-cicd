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
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Preventive controls
1. Validate and sanitize input to ensure it does not contain malicious content.
2. Use parameterized commands instead of string concatenation for the command arguments.
3. Consider using a more secure method to execute external processes if available.