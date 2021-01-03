import sys
import time
import logging
from watchdog.observers import Observer

# from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler


def on_created(event):
    print("Created")


if __name__ == "__main__":
    # logging.basicConfig(
    #     level=logging.INFO,
    #     format="%(asctime)s - %(message)s",
    #     datefmt="%Y-%m-%d %H:%M:%S",
    # )
    path = r"D:\Robi Work 2021"
    event_handler = FileSystemEventHandler()
    # calling functions
    event_handler.on_created = on_created
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        print("Monitoring")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    finally:
        observer.stop()
        observer.join()