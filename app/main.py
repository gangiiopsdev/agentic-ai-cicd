from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    return True  # Return a boolean value indicating if the host is valid

cmd_template = 'ping {}'
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        result = subprocess.run(cmd_template.format(subprocess.list2cmdline([host])), shell=False, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Invalid host"}