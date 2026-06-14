from fastapi import FastAPI
import subprocess
def execute_safe_command(command_parts):
    try:
        # Ensure that only trusted commands are executed
        if 'ping' in command_parts and all(cmd in ['ping', '-c'] for cmd in command_parts[1:]) and len(command_parts) == 3:
            result = subprocess.run(['ping'] + [arg for arg in command_parts[2:] if isinstance(arg, str)], check=True, capture_output=True, text=True)
            return result.stdout
        else:
            raise ValueError('Untrusted command detected')
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input before constructing the command
    if host.isdigit() and int(host) > 0:
        output = execute_safe_command(['-c', str(host)])
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'error', 'message': 'Invalid input'}