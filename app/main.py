from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command):
    try:
        result = subprocess.run(shlex.split(command), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    output = execute_command(command)
    return {'status': 'completed', 'output': output}