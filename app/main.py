from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return ''.join(shlex.quote(a) for a in arg.split())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate input to prevent injection attacks
        if not host.isalnum() or '-' in host:
            raise ValueError("Invalid host name")
        command = ['ping', escape_shell_arg(host)]
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}