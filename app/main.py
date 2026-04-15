import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "cp":
        if parts[1] == parts[2] or not os.path.exists(parts[1]):
            return
        with (open(f"{parts[1]}", "r") as original,
              open(f"{parts[2]}", "w") as new_file):
            new_file.write(original.read())
