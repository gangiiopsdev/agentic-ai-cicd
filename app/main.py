from fastapi import FastAPI
import subprocess
def execute_safe_command(command):
    args = command.split()
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize user input before passing to execute_safe_command
    if host.strip().isalnum():
        safe_command = f"ping {host}"
        output = execute_safe_command(safe_command)
        return {"status": "completed", "output": output}
    else:
        return {"status": "error", "message": "Invalid input"}