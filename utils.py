import os
import psutil


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def cleanLogFiles(log_directory):
    for filename in os.listdir(log_directory):
        if any(filename.endswith(ext) for ext in ['.log']):
            file_path = os.path.join(log_directory, filename)
            try:
                os.remove(file_path)  # Eliminar el archivo
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")