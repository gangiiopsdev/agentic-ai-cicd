from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Validate and sanitize the host parameter
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual whitelist logic
    if host not in allowed_hosts:
        return "Invalid input"
    try:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, timeout=5, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def safe_ping_shell(host: str):
    # Validate and sanitize the host parameter
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual whitelist logic
    if host not in allowed_hosts:
        return "Invalid input"
    try:
        result = subprocess.run(f'ping -c 1 {host}', capture_output=True, text=True, timeout=5, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class FastAPIApplication(FastAPI):
    @app.get("/ping")
    def ping(host: str):
        # Use a whitelist of allowed hosts or validate against known good patterns
        allowed_hosts = ['example.com', 'test.com']  # Replace with actual whitelist logic
        if host not in allowed_hosts:
            return "Invalid input"
        return safe_ping_shell(host)

app = FastAPIApplication()
The code already includes some validation for the host parameter, but it lacks proper sanitization and error handling. To improve security, consider using a more secure method to execute external commands, such as using a library that provides a higher-level interface for interacting with the operating system.