from fastapi import FastAPI
import subprocess
import shlex
def execute_command(command: str, *args):
    cmd_parts = [command] + list(args)
    try:
        result = subprocess.run(cmd_parts, shell=False, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Command failed with error: {e.stderr}"
def ping(host: str):
    # Validate and sanitize host input to prevent command injection
    if not validate_host(host):
        raise ValueError("Invalid host")
    return execute_command("ping", host)
def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check for allowed characters or patterns
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)