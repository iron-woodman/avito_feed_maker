import os

def delete_jpeg_files(root_directory):
    """
    Находит и удаляет JPEG файлы, содержащие "озуп" в имени, во всех подкаталогах указанного каталога.

    Args:
        root_directory (str): Путь к корневому каталогу, в котором нужно искать файлы.
    """
    for root, _, files in os.walk(root_directory):
        for file in files:
            if file.lower().endswith(".jpg"):  # Проверяем и имя, и расширение
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Удален файл: {file_path}")
                except OSError as e:
                    print(f"Ошибка при удалении файла {file_path}: {e}")

if __name__ == "__main__":
    delete_jpeg_files("company/artel/IMG/")
    # delete_jpeg_files("company/russian_fartuks/IMG/")
    # delete_jpeg_files("company/stolishnici/IMG/")

    print("Работа завершена.")
