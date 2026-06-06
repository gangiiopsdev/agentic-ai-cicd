from fastapi import FastAPI
import subprocess
def sanitize_input(host):
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    return host if host in allowed_hosts else 'localhost'

app = FastAPI()

def execute_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    command = ["ping", sanitize_input(host)]
    output = execute_command(command)
    return {"status": "completed", "output": output}