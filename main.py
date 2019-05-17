import vk_selenium
import threading
import Queue
import writing_thread
import reading_thread
import fnames


def main():
    file_names = [fnames.TEXT, fnames.LINK, fnames.IMAGE]
    file_mutex_dict = []
    for file_name in file_names:
        file_mutex_dict.append({'fname': file_name, 'thread_mutex': threading.Lock()})
    login = input("Login: ")
    password = input("Password: ")
    vk = vk_selenium.Vk(login, password)
    tables = vk.get_feeds_data()
    vk.quit()

    thread_mutex = threading.Lock()
    write_threads = []

    for i in range(len(file_names)):
        thread = writing_thread.WritingThread(new_items=tables[i], **file_mutex_dict[i])
        write_threads.append(thread)

    r_thread = reading_thread.ReadingThread(file_mutex_dict)

    for w_thread in write_threads:
        w_thread.start()

    r_thread.start()

    for thread in write_threads:
        thread.join()

    r_thread.join()


if __name__ == '__main__':
    main()
