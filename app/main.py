from fastapi import FastAPI
import os
app = FastAPI()

@app.get("/execute")
def execute_command(command: str):
    # Validate and sanitize input to prevent command injection
    safe_command = [c for c in command.split() if c.isalnum()]
    result = os.popen(' '.join(safe_command)).read()
    return {'output': result}