from fastapi import FastAPI
import subprocess
def execute_safe_command(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    return execute_safe_command(command)