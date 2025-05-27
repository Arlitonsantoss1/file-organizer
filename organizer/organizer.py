import os
import shutil

def organize_files(directory: str):
    if not os.path.isdir(directory):
        raise ValueError("Diretório inválido!")

    file_types = {
        "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
        "Documentos": [".pdf", ".docx", ".txt"],
        "Áudios": [".mp3", ".wav"],
        "Vídeos": [".mp4", ".avi"],
        "Compactados": [".zip", ".rar"],
    }

    moved_files = []

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            ext = os.path.splitext(filename)[1].lower()
            for folder, extensions in file_types.items():
                if ext in extensions:
                    folder_path = os.path.join(directory, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    dest = os.path.join(folder_path, filename)
                    shutil.move(filepath, dest)
                    moved_files.append((filename, folder))
                    break
    return moved_files
