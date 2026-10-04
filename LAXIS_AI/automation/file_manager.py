import os


class FileManager:

    def list_files(self, path):

        try:
            return os.listdir(path)

        except Exception as e:
            return str(e)