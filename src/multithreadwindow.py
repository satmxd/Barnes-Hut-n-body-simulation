import threading
from queue import Queue
import subprocess

import GUI
import simulationpygame



def run_script(script_name):
    subprocess.run(["python", script_name])

# if __name__ == "__main__":
#     q = Queue()
#     gui_thread = threading.Thread(target=run_script, args=("GUI.py",), daemon=True)
#     gui_thread.start()

#     # Run the simulation loop in the main thread
#     run_script('simulationpygame.py')

#     print("Both scripts have finished executing.")
if __name__ == "__main__":
    q = Queue()
    script1_thread = threading.Thread(target=simulationpygame.main, args=(q,))
    print(q.get())
    script2_thread = threading.Thread(target=GUI.main, args=(q,))

    script1_thread.start()
    script2_thread.start()

    script1_thread.join()
    script2_thread.join()

    print("Both scripts have finished executing.")

# if __name__ == "__main__":
#     script1_thread = threading.Thread(target=run_script, args=("simulationpygame.py",))
#     script2_thread = threading.Thread(target=run_script, args=("GUI.py",))

#     script1_thread.start()
#     script2_thread.start()

#     script1_thread.join()
#     script2_thread.join()

#     print("Both scripts have finished executing.")
