from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return input_str.replace(';', '').replace('&', '')

app = FastAPI()
def execute_command(command, arguments):
    sanitized_arguments = [subprocess.quote(arg) for arg in arguments]
    process = subprocess.Popen([command] + sanitized_arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    output, error = process.communicate()
    return output.decode(), error.decode().replace('\n', '\\n')

@app.get("/ping")
def ping(host: str):
    try:
        host = sanitize_input(host)
        output, _ = execute_command('ping', [host])
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}