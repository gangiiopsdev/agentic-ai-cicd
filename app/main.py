from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess.run with check=True and shell=False
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Preventive controls:
# 1. Validate and sanitize input to ensure it only contains allowed characters.
# 2. Use parameterized queries or prepared statements if executing SQL commands.
# 3. Limit permissions of the user running the application.
# 4. Regularly update dependencies and security patches.