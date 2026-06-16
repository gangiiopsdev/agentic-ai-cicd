from fastapi import FastAPI
import ping3

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input
    sanitized_host = sanitize_input(host)

    try:
        response_time = ping3.ping(sanitized_host, timeout=5)
        if response_time is not None:
            return {"status": "completed", "host": sanitized_host, "response_time": response_time}
        else:
            return {"status": "error", "message": "No response from host"}, 400
    except Exception as e:
        return {"status": "error", "message": str(e)}, 400