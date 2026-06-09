from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ["ping", host]
    subprocess.run(command, check=True)
    return {"status": "completed"}

# Preventive Controls:
# 1. Validate and sanitize input to ensure it only contains expected values.
# 2. Use parameterized queries or escape user inputs if applicable.
# 3. Limit the use of subprocess to trusted commands and minimize permissions.