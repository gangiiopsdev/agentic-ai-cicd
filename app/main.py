from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command_parts):
    subprocess.run(command_parts, check=True)

@app.get("/ping")
def ping(host: str):    
    # Safe implementation
    command_parts = ['ping', host]
    execute_safe_command(command_parts)

    return {"status": "completed"}