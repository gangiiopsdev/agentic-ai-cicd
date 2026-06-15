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
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Preventive controls
- Use a whitelist of allowed hosts for the ping command.
- Implement input validation to ensure that the `host` parameter only contains valid IP addresses or domain names.
- Consider using a more secure method for network operations, such as using an HTTP-based API if available.