from fastapi import FastAPI
import subprocess
def execute_safe_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    command = ['ping', '--'] + host.split(' ')
    # Validate or sanitize the input before passing it to subprocess
    if not validate_host(host):
        raise ValueError("Invalid host")
    result = execute_safe_command(command)
    return {'status': 'completed', 'result': result}
def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
    return any(host.startswith(allowed) for allowed in allowed_hosts)