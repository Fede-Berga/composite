from abc import ABC, abstractmethod

# Component Interface
class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self, indent=0):
        pass

# Leaf Class: File
class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def show_details(self, indent=0):
        print(' ' * indent + f"File: {self.name} (Size: {self.size}MB)")

# Composite Class: Folder
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def show_details(self, indent=0):
        print(' ' * indent + f"Folder: {self.name}")
        for child in self.children:
            child.show_details(indent + 2)

# Client Code
if __name__ == "__main__":
    # Create leaf objects (Files)
    file1 = File("file1.txt", 10)
    file2 = File("file2.jpg", 20)
    file3 = File("file3.mp4", 100)
    
    # Create composite objects (Folders)
    folder1 = Folder("Folder1")
    folder2 = Folder("Folder2")
    
    # Create a root folder
    root_folder = Folder("RootFolder")
    
    # Add files to folders
    folder1.add(file1)
    folder1.add(file2)
    
    folder2.add(file3)
    
    # Add folders to the root folder
    root_folder.add(folder1)
    root_folder.add(folder2)
    
    # Show the details of the entire file system structure
    root_folder.show_details()
