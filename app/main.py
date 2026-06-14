from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command: str):
    try:
        output = subprocess.run(command.split(), capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

def validate_host(host: str):
    # Add validation logic here to ensure the host is safe
    allowed_hosts = ['example.com', 'test.example.com']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        command = f"ping {host}"
        result = execute_command(command)
        return {"status": "completed", "result": result}
    else:
        return {"status": "error", "message": "Invalid host"}