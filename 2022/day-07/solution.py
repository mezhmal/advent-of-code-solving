import json
import os
from turtle import right

key_type = 'type'
key_size = 'size'
key_children = 'children'
fs_file = 'file'
fs_dir = 'dir'

filesystem = {
    key_children: {
        '/': {
            key_type: fs_dir,
            key_size: 0,
            key_children: {}
        }
    }
}
work_path = []


def get_dir(fs, path):
    if not fs or not path:
        return None
    if (len(path) > 1):
        return get_dir(fs.get(key_children, {}).get(path[:1][0]), path[1:])
    else:
        return fs.get(key_children, {}).get(path[0])


def add_children(_to, _name, _type, _size):
    work_dir_children = get_dir(filesystem, _to).get(key_children)
    work_dir_children[_name] = {
        key_type: _type,
        key_size: _size,
    }
    if _type == fs_dir:
        work_dir_children[_name][key_children] = {}


def recalcute_dir_size(path):
    work_dir = get_dir(filesystem, path)
    work_dir[key_size] = sum([child[key_size] for child in work_dir[key_children].values()])


input_filename = 'input.txt'
current_directory = os.path.dirname(__file__)

with open(os.path.join(current_directory, input_filename)) as f:
    for line in f.readlines():
        data = line.strip()
        if (data.startswith('$ cd')):
            _, _, target = data.split(' ')
            match target:
                case '/':
                    work_path = ['/']
                case '..':
                    recalcute_dir_size(work_path)
                    work_path = work_path[:-1]
                case _:
                    work_path.append(target)
        elif (data.startswith('$ ls')):
            pass
        else:
            _left, _right = data.split(' ')
            if _left == fs_dir:
                dir_name = _right
                add_children(work_path, dir_name, fs_dir, 0)
            else:
                file_size, file_name = _left, _right
                add_children(work_path, file_name, fs_file, int(file_size))

recalcute_dir_size(work_path)

# print(json.dumps(filesystem, indent=4))

# solution for part 1

upper_size_limit = 100000


def get_dir_flat_list_recursively(children):
    dir_flat_list = []
    dirs_among_children = [child_key for child_key in children.keys() if children[child_key][key_type] == fs_dir]
    for dir_name in dirs_among_children:
        nested_dir_list = get_dir_flat_list_recursively(children[dir_name][key_children])
        dir_flat_list = dir_flat_list + [(dir_name, children[dir_name][key_size])] + nested_dir_list
    return dir_flat_list


dir_flat_list = get_dir_flat_list_recursively(filesystem[key_children]['/'][key_children])
result = sum([dir_size for _, dir_size in dir_flat_list if dir_size <= upper_size_limit])

print(f"Sum of the total sizes of directories with total size of at most {upper_size_limit} is {result}")
