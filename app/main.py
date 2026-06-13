from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    command_parts = ['ping', host]
    output = execute_command(command_parts)
    return {'status': 'completed', 'output': output}