import os


def read_all_subjects():
    subjects_array = []
    all_files = {"package": os.listdir('package')}
    for key, value in enumerate(all_files, start=0):
        for file in all_files[value]:
            if not file.startswith('__'):
                path = f'{value}/{file}'
                if os.path.isdir(path):
                    subjects_array.append(file)

    return subjects_array
