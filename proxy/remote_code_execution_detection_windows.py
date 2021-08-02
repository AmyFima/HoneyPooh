import wmi
import time
import elasticsearch_functions


def get_processes():
    """
    Find all the processes running on your computer right now.
    :param: none.
    :return: the processes running on the computer at this moment.
    :rtype: array.
    """
    processes = []
    f = wmi.WMI()

    for process in f.Win32_Process():
        processes.append(f"{process.Name}")

    return processes


def restart():
    """
    Initialize the file that contains the processes in all the processes running on the computer at this moment and return them for use.
    :param: none.
    :return: the processes running on the computer at this moment.
    :rtype: array.
    """
    processes = get_processes()

    # Puts all existing processes into the file of the processes
    file = open("processes.txt", "w")
    for process in processes:
        file.write(process + "\n")

    file.close()
    return processes


def run():
    """
    Finds at any given moment if new processes have been opened.
    :param: none.
    :return: none.
    """
    all_processes = restart()
    print("Restart the processes system")

    while 1:  # Find new processes forever
        processes = get_processes()

        file = open("processes.txt", "w+")
        for process in processes:
            if process not in all_processes:
                elasticsearch_functions.add_attack('Remote Code Execution', 'http://127.0.0.1:8080/run-processes')
                all_processes.append(process)
                file.write(process + "\n")

        file.close()
        time.sleep(5)

