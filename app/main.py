from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command, *args):
    if 'ping' in command:
        return {'error': 'ping is not allowed'}
    process = subprocess.Popen([command] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    result, error = execute_safe_command('ping', host)
    if error:
        return {'status': 'error', 'message': error}
    else:
        return {'status': 'completed', 'output': result}