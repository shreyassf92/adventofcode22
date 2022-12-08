commands = []

with open("./7/input.txt") as input:
    commands = input.read().splitlines()


class MyFile:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Directoty:
    def __init__(self, name: str):
        self.name = name
        self.files = []
        self.subdirectories = []
        self.parent = None
        self.size = 0

    def cd(self, directory: str):
        if directory == "..":
            return self.parent
        else:
            for dir in self.subdirectories:
                if dir.name == directory:
                    return dir

    def ls(self, item: int) -> int:
        op1, name = item.split(" ")

        if op1 == "dir":
            sub_dir = Directoty(name)
            sub_dir.parent = self
            self.subdirectories.append(sub_dir)
        else:
            self.files.append(MyFile(name, int(op1)))


def get_dir_size_recursively(directory: Directoty, result: list):

    size = 0

    for file in directory.files:
        size += file.size

    for sub_dir in directory.subdirectories:
        size += get_dir_size_recursively(sub_dir, result)

    if size <= 100000:
        result.append(size)

    directory.size = size

    return size


def get_eligible_dirs_to_delete_recursively(
    directory: Directoty, space_to_free: int, result: list
):
    if directory.size >= space_to_free:
        result.append(directory.size)

    for sub_dir in directory.subdirectories:
        get_eligible_dirs_to_delete_recursively(sub_dir, space_to_free, result)


# format input into objects
command_index = 1
root = Directoty("/")
current_pointer = root
while command_index < len(commands):
    cmd = commands[command_index]
    if "cd" in cmd:
        current_pointer = current_pointer.cd(cmd.split(" ")[-1])
        command_index += 1
    elif "ls" in cmd:
        command_index += 1
        while command_index < len(commands) and "$" not in commands[command_index]:
            current_pointer.ls(commands[command_index])
            command_index += 1
del current_pointer

# part 1
directories_less_than_100k = []
used_space = get_dir_size_recursively(root, directories_less_than_100k)
print(sum(directories_less_than_100k))

# part 2
total_space = 70000000
app_space = 30000000
space_to_free = abs(total_space - used_space - app_space)
eligible_directories_to_delete = []
get_eligible_dirs_to_delete_recursively(
    root, space_to_free, eligible_directories_to_delete
)
print(min(eligible_directories_to_delete))
