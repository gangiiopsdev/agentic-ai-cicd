from fastapi import FastAPI
import subprocess
def execute_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_command = ['ping', host]
    output = execute_safe_command(safe_command)
    return {'status': 'completed', 'output': output}