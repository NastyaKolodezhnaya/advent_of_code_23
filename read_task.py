def read_task(file_path: str) -> list[str]:
    with open(file_path) as f:
        return f.readlines()
