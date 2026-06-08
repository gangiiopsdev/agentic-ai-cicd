from fastapi import FastAPI
import subprocess

def execute_safe_command(command_parts):
    try:
        # Ensure that only trusted commands are executed
        if 'ping' in command_parts:
            result = subprocess.run(['ping', *command_parts], check=True, capture_output=True, text=True)
            return result.stdout
        else:
            raise ValueError('Untrusted command detected')
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output = execute_safe_command([host])
    return {'status': 'completed', 'output': output}