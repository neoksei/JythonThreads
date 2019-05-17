import threading
import json


class ReadingThread(threading.Thread):
    def __init__(self, file_mutex_dict):
        threading.Thread.__init__(self)
        self.file_mutex_dict = file_mutex_dict

    def run(self):
        for element in self.file_mutex_dict:
            element['thread_mutex'].acquire()
                    
            if not os.path.exists(self.fname):
                with open(self.fname, 'w') as f:
                    f.write('[]')
                
            with open(element['fname'], 'r') as f:
                items = json.load(f)
            element['thread_mutex'].release()

            for item in items:
                print(item)
