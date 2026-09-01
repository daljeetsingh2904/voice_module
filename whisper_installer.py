import subprocess
import sys

def install(package):
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", package]
    )

packages = [
    "faster-whisper",
    "ctranslate2",
    "onnxruntime",
    "numpy",
    "av"
]

print("\nStarting Whisper Installation...\n")

for package in packages:
    try:
        print(f"Installing {package}...")
        install(package)
        print(f"{package} installed successfully.\n")

    except Exception as error:
        print(f"Error installing {package}")
        print(error)


print("Whisper installation completed.")
