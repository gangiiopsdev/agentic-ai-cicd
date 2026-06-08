from fastapi import FastAPI
import subprocess
import shlex
global process_list = {}

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # More comprehensive validation to prevent common malicious patterns
    forbidden_chars = [';', '&', '|', '<', '>', '`', '$', '\\', '/', '*', '?', '~', '{', '}', '[', ']', '^']
    return all(char not in host for char in forbidden_chars)

@app.get("/ping")
def ping(host: str):
    try:
        # Validate host to ensure it does not contain malicious input
        if not is_valid_host(host):
            raise ValueError("Invalid host")
        result = subprocess.run(["ping", shlex.quote(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Add a mechanism to prevent multiple pings from the same host simultaneously
@app.get("/check")
def check(host: str):
    if host in process_list and process_list[host].is_alive():
        return {"status": "in_progress", "message": f"Ping already running for host {host}"}
    try:
        # Validate host to ensure it does not contain malicious input
        if not is_valid_host(host):
            raise ValueError("Invalid host")
        process = subprocess.Popen(["ping", shlex.quote(host)], capture_output=True, text=True)
        process_list[host] = process
        return {"status": "completed", "message": f"Ping started for host {host}"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.on_event("shutdown")
def cleanup():
    for process in process_list.values():
        if process.is_alive():
            process.terminate()