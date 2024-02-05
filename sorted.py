
from pathlib import Path
from threading import Thread
import logging


input_source = input('Enter path of sorting folder:  ') 
input_result = input('Enter path of output folder:  ')

if not input_result:
    input_result = input_source
    output = Path(input_result).parent
    output = Path(output, 'dust')
else:
    output = Path(input_result)   

source = Path(input_source)
print(source,  output)
folders = []


def list_of_folders(path: Path) :
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            list_of_folders(el)


def move_file(path: Path):
    for el in path.iterdir():
        if el.is_file():
            print(type(el))
            ext = el.suffix[1:]
            ext_folder = output/ext
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                el.rename(ext_folder/el.name)
            except OSError :
                logging.error("Error: the path is invalid")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")

    folders.append(source)
    list_of_folders(source)
    print(folders)

    threads = []
    for folder in folders:
        th = Thread(target=move_file, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    print(f"{source} has been sorted.Folder is ready for deleting")