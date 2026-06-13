from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

@app.get("/ping")
def ping(host: str):
    command = f'ping {shlex.quote(host)}'  # Sanitize user input with shlex.quote
    output, _ = execute_command(command)
    return {'status': 'completed', 'output': output.decode()}