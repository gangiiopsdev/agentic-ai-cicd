from fastapi import FastAPI
import subprocess
def execute_safe_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get="/ping")
def ping(host: str):
    command = ['ping', host]
    result = execute_safe_command(command)
    return {'status': 'completed', 'result': result}