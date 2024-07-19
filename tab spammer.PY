import subprocess

number = int(input("How Many Tabs Would You Like to Open: "))

def crash():
    processes = []
    for _ in range(number):
        processes.append(subprocess.Popen(["start", "chrome", "https://google.com"], shell=True))
    for process in processes:
        process.wait()

crash()
