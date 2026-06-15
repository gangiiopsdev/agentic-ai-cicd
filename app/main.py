from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}' if isinstance(host, str) else None
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not host.isnumeric():
        return {
            "status": "error",
            "message": "Invalid input for host"
        }
    command = generate_ping_command(host)
    if command:
        result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
        return {
            "status": "completed",
            "output": result.stdout,
            "error": result.stderr
        }
    else:
        return {
            "status": "error",
            "message": "Invalid input for host"
        }