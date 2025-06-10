import PyInstaller.__main__

if __name__ == "__main__":
    PyInstaller.__main__.run(
        [
            "main.py",
            "-p",
            "src",
            "--add-data",
            "config:config",
            "--clean",
        ]
    )
