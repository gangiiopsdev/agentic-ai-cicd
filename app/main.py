from fastapi import FastAPI
import subprocess
import shlex

def sanitize_input(input_str):
    return input_str.replace(';', '').replace('&', '')

app = FastAPI()

def execute_command(command, arguments):
    sanitized_arguments = [shlex.quote(arg) for arg in arguments]
    process = subprocess.Popen([command] + sanitized_arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    output, error = process.communicate()
    return output.decode(), error.decode().replace('\n', '\n')

@app.get("/ping")
def ping(host: str):
    try:
        host = sanitize_input(host)
        if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
            raise ValueError("Invalid hostname")
        output, _ = execute_command('ping', [host])
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}