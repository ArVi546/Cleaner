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

def convert(size, type_count):
    type = 1024**(type_count+1)
    size /= type
    return float(f"{size:.2f}")

def dir_size(bts, ending='B'):
    for item in ["", "K", "M", "G", "T", "P"]:
        if bts < 1024:
            return f"{bts:.2f} {item}{ending}"
        bts /= 1024

def counting(direct, type_count, field):
    paths.clear()
    direct = Path(direct)
    files = []
    total = 0

    for child in direct.iterdir():
        total += get_size(child)
        if convert(get_size(child), type_count) >= field:
            paths.append(child)
            files.append(f"{child.name} -> {convert(get_size(child), type_count)} {types_of_count[type_count]}")
    return files, dir_size(total)




#C:/ProgramData/Microsoft