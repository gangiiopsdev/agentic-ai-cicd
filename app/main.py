from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import Any, Dict, Union

app = FastAPI()

def sanitize_input(input: str) -> str:
    return ''.join(filter(str.isalnum, input))

@app.get("/ping")
def ping(host: str) -> Dict[str, Union[str, Dict[str, str]]]:
    sanitized_host = quote(sanitize_input(host))
    try:
        result = subprocess.run(["ping", sanitized_host], timeout=5, check=True, capture_output=True, text=True)
        return {"status": "completed", "result": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}