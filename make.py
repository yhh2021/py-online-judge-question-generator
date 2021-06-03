#!/usr/bin/env python3

from __future__ import annotations # Pre 3.9
import os
from typing import Union
from make_problem_json import get_case_input_dat_count

SAMPLE_COUNT = 3
TESTCASE_COUNT = 5
UPLOAD_DIR = 'upload'
SAMPLE_DIR = 'sample'
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

def get_case_list() -> list[str]:
    result = [ ]
    
    for i in os.listdir():
        if '.py' not in i:
            continue
        if len(i) != len('###.py') or i.split('.')[1] != 'py':
            continue

        no = i.split('.')[0]
        if not no.isdigit():
            continue
        
        result.append(i)
        
    return result

if __name__ == '__main__':
    main_targets = [ ]
    folders_to_create = [ ]

    for i in get_case_list():   
        no = i.split('.')[0]
        target = f'pp{no}'
        count = len(main_targets)
        home = f'{UPLOAD_DIR}/{count}'
        sample_home = f'{SAMPLE_DIR}/{count}'
        targets = [ ]
        input_dat_count = get_case_input_dat_count(i)
  
        # folders
        folders_to_create += [ home, f'{home}/testcase/', sample_home ]

        # .in & .out
        for k in range(TESTCASE_COUNT):
            j = k + 1
            targets.append(f'{home}/testcase/{j}.in')
            targets.append(f'{home}/testcase/{j}.out')
            add_target(f'{home}/testcase/{j}.in', '',
                       f'./make_input.py {input_dat_count} > {home}/testcase/{j}.in')
            add_target(f'{home}/testcase/{j}.out', f'{home}/testcase/{j}.in',
                       f'python3 {i} < {home}/testcase/{j}.in > {home}/testcase/{j}.out')
       
        # problem.json
        add_target(f'{home}/problem.json', '',
            f'./make_problem_json.py {i} {home}/testcase {sample_home} > {home}/problem.json')
        targets.append(f'{home}/problem.json')

        # master target
        add_target(target, targets + [ f'{home}/problem.json' ],
                  '')
        main_targets.append(target)
        
    add_target('all', [ 'prepare_dir' ] + main_targets, '')
    add_target('prepare_dir', '',
            [ f'mkdir -p {i}' for i in folders_to_create ])
    print('\n\n'.join(makefile))