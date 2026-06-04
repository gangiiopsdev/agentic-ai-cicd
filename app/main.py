from fastapi import FastAPI
import subprocess
def execute_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed: {e.output}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command_parts = ['ping', host]
    result = execute_safe_command(command_parts)
    return {'status': 'completed', 'result': result}