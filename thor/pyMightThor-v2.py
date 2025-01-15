from pathlib import Path
import logging
from glob import glob
import os
import shutil

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def debug_print(var_name: str, var_value) -> None:
    logging.debug("{}: {} ({})".format(var_name, var_value, type(var_value)))

def remove_empty_thor_directories(base_path: str) -> None:
    dir_paths = glob(base_path + "*/")
    debug_print('dir_paths', dir_paths)
    
    for dir_path in dir_paths:
        dir_path = Path(dir_path)
        debug_print('dir_path', dir_path)
        
        if 'thor_' in dir_path.name:
            items = list(dir_path.iterdir())
            files = [f for f in items if f.is_file()]
            subdirs = [d for d in items if d.is_dir()]
            
            if not files and len(subdirs) == 1 and subdirs[0].name == "sans":
                try:
                    # Use shutil.rmtree() to forcefully remove the entire directory tree
                    shutil.rmtree(str(dir_path))
                    logging.info("Successfully removed {}".format(dir_path))
                except OSError as error:
                    logging.error("Error removing directory {}: {}".format(dir_path, error))

if __name__ == '__main__':
    setup_logging()
    TOP_DIR_PATH = '/media/qnap/'
    remove_empty_thor_directories(TOP_DIR_PATH)