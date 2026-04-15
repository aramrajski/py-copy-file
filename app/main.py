import os


def copy_file(command: str) -> None:
    parts = command.split()
    src = parts[1]
    dst = parts[2]
    if len(parts) == 3 and parts[0] == "cp":
        if src == dst or not os.path.exists(src):
            return
        with (open(f"{src}", "r") as org, open(f"{dst}", "w") as new):
            new.write(org.read())
