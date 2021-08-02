from datetime import datetime
import time
import subprocess
import elasticsearch_functions
import get_config_data


def get_processes():
    """
    Find all the processes running on your computer right now.
    :param: none.
    :return: the processes running on the computer at this moment.
    :rtype: array.
    """
    processes = []
    output = str(subprocess.check_output(['ps', '-ef']).decode()).split('\n')[1:-1:1]

    for process in output:
        process_name = str(str(process.split(' ?        ')[-1])[8::1])
        if len(process_name.split(':')) < 2 and 'ps -ef' not in process:
            processes.append(process_name)

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
    with open("processes.txt", "a+") as file:
        for process in processes:
            file.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\t' + process + "\n")

    return processes


def run():
    """
    Finds at any given moment if new processes have been opened.
    :param: none.
    :return: none.
    """
    elasticsearch_functions.open_processes_index()
    server_port = get_config_data.get_server_port()
    all_processes = restart()

    for process in all_processes:
        elasticsearch_functions.add_process(process)

    while 1:  # Find new processes forever
        processes = get_processes()

        for process in processes:
            if process not in all_processes:
                elasticsearch_functions.add_process(process)
                elasticsearch_functions.add_attack('Remote Code Execution', f'http://127.0.0.1:{server_port}/run-processes')
                print(f"attack: Remote Code Execution    {process}")
                all_processes.append(process)

                with open("processes.txt", "a+") as file:
                    file.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\t' + process + '\n')

        try:
            time.sleep(5)
        except KeyboardInterrupt as e:
            pass

