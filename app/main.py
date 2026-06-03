from fastapi import FastAPI
import subprocess
global_params = {
    'ping': ['-c', '1'],
    # Add more commands as needed
}

def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Basic validation to prevent command injection
        return {"status": "error", "output": "Invalid input"}
    sanitized_host = subprocess.list2cmdline([host])
    command = global_params['ping'] + [sanitized_host]
    output = run_command(command)
    return {"status": "completed", "output": output}