def removeVirus(s):
    parts = s.split(":")
    prefix = parts[0].strip()
    file_part = parts[1].strip()

    files = [f.strip() for f in file_part.split(",")]

    safe_files = []
    for file in files:
        lower_file = file.lower()
        if ("virus" in lower_file or "malware" in lower_file) and not ("antivirus" in lower_file or "notvirus" in lower_file):
            continue
        safe_files.append(file)

    if not safe_files:
        return f"{prefix}: Empty"
    return f"{prefix}: {', '.join(safe_files)}"


print(removeVirus("PC Files: spotifysetup.exe, virus.exe, dog.jpg"))
print(removeVirus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe "))
print(removeVirus("PC Files: notvirus.exe, funnycat.gif"))
