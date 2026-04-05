from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as req:
        return [line.strip() for line in req if line.strip() and not line.startswith("#")]

setup(
    name="personal-cli-assistant-bot",
    version="1.0.0",                    
    description="CLI Personal Assistant for managing contacts and notes",
    author="Serhii",          
    packages=find_packages(),           
    install_requires=read_requirements(), 
    entry_points={
        "console_scripts": [
            "assistant = bot.main:main", 
        ],
    },
)