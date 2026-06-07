from fastapi import FastAPI
import subprocess
app = FastAPI()

@app.get("/execute")
def execute_command(command: str):
    # Validate and sanitize input to prevent command injection
    safe_command = [c for c in command.split() if c.isalnum()]
    result = subprocess.run(safe_command, capture_output=True, text=True)
    return {'output': result.stdout}