from fastapi import FastAPI
import subprocess
def execute_safe_command(command, args):
    try:
        output = subprocess.run([command] + args, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not validate_host(host):
        raise ValueError("Invalid host")
    result = execute_safe_command('ping', [host])
    return {"status": "completed", "result": result}

def validate_host(host: str) -> bool:
    # Add your validation logic here, e.g., check for allowed IP ranges or domain names
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts