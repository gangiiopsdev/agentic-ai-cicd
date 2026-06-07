from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command: str):
    try:
        # Sanitize command input by whitelisting allowed commands or using a safer method like Paramiko for SSH.
        if not is_allowed_command(command):
            raise ValueError("Command is not allowed")
        result = subprocess.run(shlex.split(command), capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Consider using a safer method for pinging, like Paramiko or ICMP.
    command = f'ping {host}'
    result = execute_command(command)
    return {"status": "completed", "result": result}

# Function to check if the command is allowed (example implementation)
def is_allowed_command(command: str) -> bool:
    allowed_commands = ["ping"]
    return command in allowed_commands