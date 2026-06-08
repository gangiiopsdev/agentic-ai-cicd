from fastapi import FastAPI
import subprocess
def execute_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, check=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command_parts = ["ping", host]
    result = execute_safe_command(command_parts)
    return {"status": "completed", "result": result}