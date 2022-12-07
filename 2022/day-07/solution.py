import os
import time


key_type = 'type'
key_size = 'size'
key_children = 'children'
fs_file = 'file'
fs_dir = 'dir'


def get_dir(fs, path):
    if not fs or not path:
        return None
    if (len(path) > 1):
        return get_dir(fs.get(key_children, {}).get(path[:1][0]), path[1:])
    else:
        return fs.get(key_children, {}).get(path[0])


def add_children(fs, _to, _name, _type, _size):
    work_dir_children = get_dir(fs, _to).get(key_children)
    work_dir_children[_name] = {
        key_type: _type,
        key_size: _size,
    }
    if _type == fs_dir:
        work_dir_children[_name][key_children] = {}


def recalcute_dir_size(fs, path):
    work_dir = get_dir(fs, path)
    work_dir[key_size] = sum([child[key_size] for child in work_dir[key_children].values()])


def get_dir_flat_list_recursively(children):
    dir_flat_list = []
    dir_names = [child_key for child_key in children.keys() if children[child_key][key_type] == fs_dir]
    for dir_name in dir_names:
        nested_dir_list = get_dir_flat_list_recursively(children[dir_name][key_children])
        dir_flat_list = dir_flat_list + [(dir_name, children[dir_name][key_size])] + nested_dir_list
    return dir_flat_list


def main():
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
                        recalcute_dir_size(filesystem, work_path)
                        work_path = work_path[:-1]
                    case _:
                        work_path.append(target)
            elif (data.startswith('$ ls')):
                pass
            else:
                _left, _right = data.split(' ')
                if _left == fs_dir:
                    dir_name = _right
                    add_children(filesystem, work_path, dir_name, fs_dir, 0)
                else:
                    file_size, file_name = _left, _right
                    add_children(filesystem, work_path, file_name, fs_file, int(file_size))

    recalcute_dir_size(filesystem, work_path)
    recalcute_dir_size(filesystem, ['/'])

    # solution for part 1

    upper_size_limit = 100000

    dir_flat_list = get_dir_flat_list_recursively(filesystem[key_children]['/'][key_children])
    result = sum([dir_size for _, dir_size in dir_flat_list if dir_size <= upper_size_limit])

    print(f"(part 1) Sum of the total sizes of directories with total size of at most {upper_size_limit} is {result}")

    total_disk_space = 70000000
    required_for_update_space = 30000000
    used_space = filesystem[key_children]['/'][key_size]
    need_extra_space = required_for_update_space - (total_disk_space - used_space)

    sorted_dir_flat_list = sorted(dir_flat_list, key=lambda dir: dir[1])
    result2 = 0
    for _, size in sorted_dir_flat_list:
        if size > need_extra_space:
            result2 = size
            break

    print(f"(part 1) For free up enough space need to delete directory with size {result2}")


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print()
    print(f"Done in {stop-start:0.4f} seconds")
