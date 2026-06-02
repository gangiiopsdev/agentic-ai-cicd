from fastapi import FastAPI
import subprocess
import re

# Define allowed characters
allowed_chars = r'[a-zA-Z0-9.-_!@#$%^&*()+=\[\]{}|;:,.<>?]'