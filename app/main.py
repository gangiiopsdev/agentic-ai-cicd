from fastapi import FastAPI
import re

def sanitize_input(input_string):
    allowed_chars = r'^[a-zA-Z0-9.-]+$'
    return re.sub(r'[^' + allowed_chars + ']', '', input_string)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Import os module to use os.path.abspath for absolute path