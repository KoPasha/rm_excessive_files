import sys


def main():
    if len(sys.argv) > 1:
        files_pattern = sys.argv[1]
        make_cur_folder_slimmer_by_deleting_excessive_files(files_pattern)
    else:
        print('You have to put some filename pattern as an argument, otherwise it wouldn\'t work')

def make_cur_folder_slimmer_by_deleting_excessive_files(files_pattern):
    files = find_all_files(files_pattern)
    files_to_delete = sortout_files_for_deletion(files)
    delete_files(files_to_delete)

def find_all_files(files_pattern):
    pass
def sortout_files_for_deletion(files):
    pass
def delete_files(files_to_delete):
    pass

if __name__ == '__main__':
    main()
