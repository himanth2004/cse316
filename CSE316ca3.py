class FileSystem:
    def __init__(self, total_blocks):
        self.disk = [None] * total_blocks
        self.total_blocks = total_blocks
        self.used_blocks = 0

    def add_file(self, name, size):
        free_blocks = [i for i, block in enumerate(self.disk) if block == None]
        if len(free_blocks) >= size:
            for i in free_blocks[:size]:
                self.disk[i] = name
            self.used_blocks += size
            return True
        else:
            return False

    def delete_file(self, name):
        if name in self.disk:
            self.disk = [None if block == name else block for block in self.disk]
            self.used_blocks -= self.disk.count(None)
            return True
        else:
            return False

    def rename_file(self, old_name, new_name):
        if old_name in self.disk:
            self.disk = [new_name if block == old_name else block for block in self.disk]
            return True
        else:
            return False

    def move_file(self, name, new_location):
        size = self.disk.count(name)
        free_blocks = [i for i, block in enumerate(self.disk[new_location:]) if block == None]
        if len(free_blocks) >= size:
            for i in [i + new_location for i in free_blocks[:size]]:
                self.disk[i] = name
            for i in [i for i, block in enumerate(self.disk) if block == name]:
                if i < new_location or i >= new_location + size:
                    self.disk[i] = None
            return True
        else:
            return False

    def calculate_fragmentation(self):
        free_blocks = self.disk.count(None)
        return free_blocks


fs = FileSystem(1024)

print(
    "0)To Stop the simulation\n1) Creating a File\n2) Deleting a File\n3) Renaming a File\n4) Moving a File\n5) Calculate Fragmentation")
print('Enter the number of your Choice')




while True:
    choice = input("Enter Choice: ")
    if choice == '1':
        name = input("Enter name of file: ")
        size = int(input("Enter size of file in MB: "))
        if fs.add_file(name, size):
            print("The file has been added successfully.")
        else:
            print("The file has not been added successfully due to insufficient space.")

    elif choice == '2':
        name = input("Enter name of file to be removed: ")
        if fs.delete_file(name):
            print("The file has been successfully removed.")
        else:
            print("The file was not removed successfully because it does not exist.")

    elif choice == '3':
        old_name = input("Enter old name of file to be renamed : ")
        new_name = input("Enter new name of file to be renamed : ")
        if fs.rename_file(old_name, new_name):
            print("The file has been successfully renamed.")
        else:
            print("The file was not renamed because it does not exist.")

    elif choice == '4':
        name = input("Enter name of file to be moved: ")
        new_location = int(input("Enter the location at which you need to move the file: "))
        if fs.move_file(name, new_location):
            print("The file has been successfully moved to the new location.")
        else:
            print("The file does not exist or there is not enough space at the new location.")
    elif choice == '5':
        print("No. of Fragmented blocks are: {}".format(fs.calculate_fragmentation()))
    else:
        break
