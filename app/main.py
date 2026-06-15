from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    return [arg for arg in user_input.split() if arg.isalnum()]

app = FastAPI()
def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error
def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return True
    else:
        return False
@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get="/ping"
def ping(host: str):
    if validate_host(host):
        sanitized_host = sanitize_input(host)
        command = ["ping"] + sanitized_host
        output, error = execute_command(command)
        if error:
            return {"status": "failed", "error": error.decode()}
        else:
            return {"status": "completed", "output": output.decode()}
    else:
        return {"status": "failed", "error": "Invalid host"}