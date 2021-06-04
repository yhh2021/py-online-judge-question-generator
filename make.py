#!/usr/bin/env python3

from __future__ import annotations # Pre 3.9
import os
from typing import Union
from make_problem_json import get_case_input_dat_count

SAMPLE_COUNT = 3
TESTCASE_COUNT = 5
UPLOAD_DIR = 'upload'
SAMPLE_DIR = 'sample'
CASES_DIR = 'cases'
makefile = [ ]

def add_target(name: str, dependencies: Union[ list[str], str ],
               commands: Union[ list[str], str ]) -> None:
    global makefile
    
    if isinstance(dependencies, str):
        dependencies = [ dependencies ]
    if isinstance(commands, str):
        commands = [ commands ]
    
    makefile.append(f'{name}: {" ".join(dependencies)}\n' +
                   '\n'.join([ f'\t{i}' for i in commands ]))

def is_case_filename_valid(filename: str) -> bool:
    if '.py' not in filename:
        return False
    
    parts = filename.split('.')
    if len(parts) != 2:
        return False
    
    no, ext = parts
    if len(filename) != len('###.py') or ext != 'py' or not no.isdigit():
        return False

    return True

def get_case_list() -> list[str]:
    return [ i for i in os.listdir(CASES_DIR) if is_case_filename_valid(i) ]

def assert_folder_empty(folder: str) -> None:
    assert len(os.listdir(folder)) == 0, f"target folder '{folder}' not empty"

def make_in_out_files(folder: str, num: int) -> list[str]:
    targets = [ ]

    for k in range(num):
        j = k + 1
        targets.append(f'{folder}/{j}.in')
        targets.append(f'{folder}/{j}.out')
        add_target(f'{folder}/{j}.in', '',
                   f'./make_input.py {input_dat_count} > {folder}/{j}.in')
        add_target(f'{folder}/{j}.out', f'{folder}/{j}.in',
                   f'python3 {case_filename_full} < {folder}/{j}.in > {folder}/{j}.out')

    return targets

if __name__ == '__main__':
    main_targets = [ ]
    folders_to_create = [ ]

    assert_folder_empty(UPLOAD_DIR)
    
    for case_filename in get_case_list():   
        no = case_filename.split('.')[0]
        case_filename_full = f'{CASES_DIR}/{case_filename}'
        target = f'pp{no}'
        main_targets.append(target)
        count = len(main_targets)
        home = f'{UPLOAD_DIR}/{count}'
        sample_home = f'{SAMPLE_DIR}/{count}'
        targets = [ ]
        input_dat_count = get_case_input_dat_count(case_filename_full)
  
        # folders
        folders_to_create += [ home, f'{home}/testcase/', sample_home ]

        # .in & .out
        targets += make_in_out_files(f'{home}/testcase', TESTCASE_COUNT)
        targets += make_in_out_files(sample_home, SAMPLE_COUNT)
        
        # problem.json
        add_target(f'{home}/problem.json', '',
            f'./make_problem_json.py {case_filename_full} {home}/testcase {sample_home} > {home}/problem.json')
        targets.append(f'{home}/problem.json')

        # master target
        add_target(target, targets + [ f'{home}/problem.json' ],
                  '')
        
    add_target('all', [ 'prepare_dir' ] + main_targets, '')
    add_target('prepare_dir', '',
            [ f'mkdir -p {i}' for i in folders_to_create ])
    print('\n\n'.join(makefile))
