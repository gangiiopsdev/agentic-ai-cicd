from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command):
    try:
        completed_process = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return completed_process.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get="/ping")
def ping(host: str):
    command = ['ping', host]
    result = execute_safe_command(command)
    return {'status': 'completed', 'result': result}