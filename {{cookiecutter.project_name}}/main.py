import os
import runpy
import sys

from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, os.getenv("PYTHONPATH", "src"))

if __name__ == "__main__":
    runpy.run_module("{{cookiecutter.project_slug}}", run_name="__main__")
