from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command_parts):
    # Use check_output instead of run if you need to capture the output
    result = subprocess.check_output(command_parts, stderr=subprocess.STDOUT)
    return result.decode('utf-8')

@app.get("/ping")
def ping(host: str):    
    # Validate and sanitize input
    if not host.strip():
        raise ValueError("Host parameter is required")
    command_parts = ['ping', f'{-host}']  # Sanitize input by using a formatted string to ensure the command structure is correct
    output = execute_safe_command(command_parts)
    return {"status": "completed", "output": output}