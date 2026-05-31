from fastapi import FastAPI
import subprocess
class SanitizeFilter:
    @staticmethod
def sanitize_input(input_string):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_!@#$%^&*()+=[]{}|;:,.<>?/`'
        return ''.join(char for char in input_string if char in allowed_chars)

app = FastAPI()

class PingController:
    @staticmethod
def ping(host: str):
        sanitized_host = SanitizeFilter.sanitize_input(host)
        subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}