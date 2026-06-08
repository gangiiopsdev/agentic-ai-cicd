from fastapi import FastAPI
import subprocess
app = FastAPI()

def validate_command(command: str) -> bool:
    return all(c.isalnum() for c in command)

@app.get("/execute")
def execute_command(command: str):
    if not validate_command(command):
        raise ValueError("Invalid command")
    safe_command = [c for c in command.split() if c.isalnum()]
    result = subprocess.run(safe_command, capture_output=True, text=True)
    return {'output': result.stdout}