from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the input to ensure it only contains allowed characters and does not exceed a reasonable length
        if not re.match(r'^[a-zA-Z0-9-.]{1,256}$', host):  # Adjust regex pattern as needed
            raise ValueError("Invalid input")
        command = ['ping', shlex.quote(host)]  # Use shlex.quote to safely escape the host input
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}