import os
import hashlib
import time
import datetime
import threading


class File:
    def __init__(self, filename, filepath):
        self.filename = filename
        self.filepath = filepath
        self.created_time = self.get_created_time()
        self.updated_time = self.get_updated_time()

    def get_created_time(self):
        return datetime.datetime.fromtimestamp(os.path.getctime(self.filepath)).strftime('%Y-%m-%d %H:%M:%S')

    def get_updated_time(self):
        return datetime.datetime.fromtimestamp(os.path.getmtime(self.filepath)).strftime('%Y-%m-%d %H:%M:%S')

    def info(self):
        pass


class TextFile(File):
    def __init__(self, filename, filepath):
        super().__init__(filename, filepath)
        self.line_count = self.get_line_count()
        self.word_count = self.get_word_count()
        self.char_count = self.get_char_count()

    def get_line_count(self):
        with open(self.filepath, 'r') as file:
            return sum(1 for _ in file)

    def get_word_count(self):
        with open(self.filepath, 'r') as file:
            return sum(len(line.split()) for line in file)

    def get_char_count(self):
        with open(self.filepath, 'r') as file:
            return sum(len(line) for line in file)

    def info(self):
        print(f"{self.filename} (txt):")
        print(f"  Created: {self.created_time}")
        print(f"  Updated: {self.updated_time}")
        print(f"  Line count: {self.line_count}")
        print(f"  Word count: {self.word_count}")
        print(f"  Character count: {self.char_count}")

class ImageFile(File):
    def __init__(self, filename, filepath):
        super().__init__(filename, filepath)
        self.image_size = self.get_image_size()

    def get_image_size(self):
        with open(self.filepath, 'rb') as file:
            image_data = file.read()
            return len(image_data)

    def info(self):
        print(f"{self.filename} (png):")
        print(f"  Created: {self.created_time}")
        print(f"  Updated: {self.updated_time}")
        print(f"  Image size: {self.image_size} bytes")

class ProgramFile(File):
    def __init__(self, filename, filepath):
        super().__init__(filename, filepath)
        self.line_count = self.get_line_count()
        self.class_count = self.get_class_count()
        self.method_count = self.get_method_count()

    def get_line_count(self):
        with open(self.filepath, 'r') as file:
            return sum(1 for _ in file)

    def get_class_count(self):
        # Placeholder for class count detection (e.g., using regex)
        return 0

    def get_method_count(self):
        # Placeholder for method count detection (e.g., using regex)
        return 0

    def info(self):
        print(f"{self.filename} (py):")
        print(f"  Created: {self.created_time}")
        print(f"  Updated: {self.updated_time}")
        print(f"  Line count: {self.line_count}")
        print(f"  Class count: {self.class_count}")
        print(f"  Method count: {self.method_count}")

class FolderMonitor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.file_snapshots = {}
        self.current_snapshot_time = None

    def create_snapshot(self):
        self.current_snapshot_time = time.strftime('%Y-%m-%dT%H:%M:%S.%f')
        print(f"Created Snapshot at: {self.current_snapshot_time}")

        self.file_snapshots.clear()

        for filename in os.listdir(self.folder_path):
            filepath = os.path.join(self.folder_path, filename)

            if os.path.isfile(filepath):
                file_type = self.get_file_type(filename)
                
                if file_type == 'txt':
                    file_obj = TextFile(filename, filepath)
                elif file_type == 'png':
                    file_obj = ImageFile(filename, filepath)
                elif file_type == 'py':
                    file_obj = ProgramFile(filename, filepath)
                
                self.file_snapshots[filename] = file_obj

    def get_file_type(self, filename):
        _, file_extension = os.path.splitext(filename)
        return file_extension[1:]

    def info(self, filename):
        if filename in self.file_snapshots:
            self.file_snapshots[filename].info()
        else:
            print(f"{filename} not found")

    def status(self):
        print(f"Snapshot at: {self.current_snapshot_time}")
        for filename, file_obj in self.file_snapshots.items():
            updated_time = file_obj.get_updated_time()
            if updated_time > self.current_snapshot_time:
                print(f"{filename} Changed")
            else:
                print(f"{filename} No Change")

    def detect_changes(self):
        while True:
            time.sleep(5)
            for filename, file_obj in self.file_snapshots.items():
                updated_time = file_obj.get_updated_time()
                if updated_time > self.current_snapshot_time:
                    print(f"{filename} Changed")
                    self.current_snapshot_time = updated_time
                    
folder_path = 'C:/path/to/your/folder'  # Replace with your folder path
folder_monitor = FolderMonitor(folder_path)

detection_thread = threading.Thread(target=folder_monitor.detect_changes)
detection_thread.start()

while True:
    command = input("Enter command (commit/info <filename>/status/exit): ")

    if command == 'commit':
        folder_monitor.create_snapshot()
    elif command.startswith('info'):
        _, filename = command.split(' ', 1)
        folder_monitor.info(filename)
    elif command == 'status':
        folder_monitor.status()
    elif command == 'exit':
        break
    else:
        print("Invalid command")
