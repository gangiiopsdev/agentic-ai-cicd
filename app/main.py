from fastapi import FastAPI
import subprocess
def execute_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ('.', '-'))
@app.get("/ping")
def ping(host: str):  
    sanitized_host = sanitize_input(host)
    command = ["ping", sanitized_host]
    result = execute_command(command)
    return {"status": "completed", "output": result}