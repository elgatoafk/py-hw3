import os
import shutil
from concurrent.futures import ThreadPoolExecutor
import time
import logging

logging.basicConfig(filename=os.path.expanduser('log'), level=logging.DEBUG, format='%(threadName)s %(message)s')
logger = logging.getLogger("MyLogger")


def logging_wrapper(func):
    def wrapped(*args, **kwargs):
        logger.info("Func name: {0}".format(func.__name__))
        func(*args, **kwargs)
    return wrapped

def copy_file(source_file, target_dir):
    
    try:
        shutil.copy(source_file, target_dir)
        
    except Exception as e:
        print(f"Failed to copy {source_file}: {e}")

def copy_files_by_extension(source_dir, target_dir="dist"):
    
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    
    with ThreadPoolExecutor() as executor:
        
        for root, _, files in os.walk(source_dir):
            for file in files:
                
                source_file_path = os.path.join(root, file)

                _, extension = os.path.splitext(file)
                                
                target_subdir = os.path.join(target_dir, extension[1:])
                if not os.path.exists(target_subdir):
                    os.makedirs(target_subdir)

               
                executor.submit(logging_wrapper(copy_file), source_file_path, target_subdir)
        
        
if __name__ == "__main__":
 start_time = time.perf_counter()
 copy_files_by_extension(r"C:\Users\Я\Downloads\hlam")

 end_time = time.perf_counter()
 print(f"Program finished in {end_time-start_time} seconds")
