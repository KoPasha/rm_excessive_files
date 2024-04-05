import sys
import os
import re

def main():
    if len(sys.argv) > 1:
        files_pattern = sys.argv[1]
        #what is a pattern: any sequence of letter and numbers, starting with letter
        # no special symbols !
        make_cur_folder_slimmer_by_deleting_excessive_files(files_pattern)
    else:
        print('You omitted parameter for this utility, thus the default file name pattern will be used ""fileStorage4_1c""')
        make_cur_folder_slimmer_by_deleting_excessive_files('fileStorage4_1c')

def make_cur_folder_slimmer_by_deleting_excessive_files(files_pattern):
    path_to_search_in = os.getcwd()
    files = find_all_files(path_to_search_in)
    files_all = find_files_that_fit('{}{}'.format(files_pattern,'_all'), files)
    files_dif = find_files_that_fit('{}{}'.format(files_pattern,'_dif'), files)
    files_to_delete = sortout_files_for_deletion(files_all,files_dif,files_pattern)
    delete_files(files_to_delete)

def filename_fits_patten(cur_file,filename_comparison):
    result_of_search = filename_comparison.search(cur_file)
    if result_of_search:
        return True
    else:
        return False

def find_all_files(path_to_search_in):
    files_in_cur_dir = [f for f in os.listdir(path_to_search_in) if os.path.isfile(os.path.join(path_to_search_in,f))]
    return files_in_cur_dir


def find_files_that_fit(files_pattern, files):
    files_that_fit_to_pattern = []
    files_pattern_full = r'{}\d*\.rar'.format(files_pattern)
    filename_comparison_full = re.compile(files_pattern_full)
    for cur_file_original in files:
        cur_file = cur_file_original.replace('\uf00d','')
        if filename_fits_patten(cur_file,filename_comparison_full):
            files_that_fit_to_pattern.append(cur_file)
    return files_that_fit_to_pattern

def sortout_files_for_deletion(files_all,files_dif,files_pattern):
    #first of all we should find latest _all_ file and get it out from the list
    files_all.sort()
    latest_element = files_all.pop()
    latest_element_for_dif = latest_element.replace('_all','_dif')
    result = files_all.copy()
    for cur_dif in files_dif:
        if cur_dif < latest_element_for_dif:
            result.append(cur_dif)
    return result

def delete_files(files_to_delete):
    if len(files_to_delete) == 0:
        print('Havn\'t found any files for deletion')
    else:
        for cur_file in files_to_delete:
            if cur_file != '' and os.path.exists(cur_file):
                os.remove(cur_file)
                print('file {} is removed'.format(cur_file))
            else:
                print('file {} does not exist'.format(cur_file))

if __name__ == '__main__':
    main()
