from fastapi import FastAPI
import subprocess
from shlex import quote
generate_random_string = lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=10))

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> Dict[str, Union[str, Dict[str, str]]]:
    random_str = generate_random_string()
    try:
        result = subprocess.run(["ping", f'host_{random_str}'], timeout=5, check=True, capture_output=True, text=True)
        return {"status": "completed", "result": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}