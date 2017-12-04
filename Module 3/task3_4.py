# TASK:
# Розробити функцію file_search(folder, filename),
# яка приймає 2 аргументи -- список folder та рядок filename,
# та повертає рядок -- повний шлях до файлу або папки filename в структурі folder.

# SOLUTION:
def file_search(folder, filename):
    # if current directory/folder is the one, return it
    if folder == filename:
        return filename
    else:
        # check if it is file or folder
        if isinstance(folder, list):
            # check if 0-element (foldername) is the one
            # and return if it is
            if folder[0] == filename:
                return filename
            # otherwise, looping through directory
            # ignoring first argument
            for i in folder[1:]:
                # use recursion for each element
                path = file_search(i, filename)
                # if return value is string
                if isinstance(path, str):
                    # write current directory and return to higher level
                    return folder[0] + '/' + path
                # if False was return - nothing here
            # if loop is finished and we still in function - return False
            return False
        # if it is file, nothing here, return False
        else:
            return False
