from pathlib import Path

types_of_count = ["KB", "MB", "GB"]
paths = []

def get_size(path):
    volume = 0
    try:
        if path.is_dir():
            for file in path.iterdir():
                if not file.is_dir():
                    volume += file.stat().st_size
                elif file.is_dir():
                    volume += get_size(file)
            return volume
        else:
            return path.stat().st_size
    except OSError:
        return 0

def to_MB(size, type_count):
    type = 1024**(type_count+1)
    return float(str(size//type) + "." + str(size%type)[:2])


def counting(direct, type_count, field):
    paths.clear()
    direct = Path(direct)
    files = []
    for child in direct.iterdir():
        if to_MB(get_size(child), type_count) >= field:
            paths.append(child)
            files.append(f"{child.name} -> {to_MB(get_size(child), type_count)} {types_of_count[type_count]}")
    return files




#C:/ProgramData/Microsoft