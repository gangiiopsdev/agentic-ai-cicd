from fastapi import FastAPI
import subprocess
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=False)
    output, error = process.communicate()
    return output, error
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
    return host in allowed_hosts
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host"}
    command = ["ping", host]
    result, error = run_command(command)
    if error:
        return {"status": "failed", "error": error}
    else:
        return {"status": "completed", "result": result}