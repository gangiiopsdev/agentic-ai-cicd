from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command: list):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping(host: str):
    try:
        host = shlex.quote(host)
        command = ['ping', host]
        result = execute_command(command)
        return {'status': 'completed', 'result': result}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}