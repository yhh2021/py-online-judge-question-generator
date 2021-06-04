#!/usr/bin/env python3

from __future__ import annotations # Pre 3.9
import argparse
import os
import abbrs


title, description, in_count = '', [ ], -1

def get_script_information(filename: str) -> None:
    global title, description, in_count

    lines = abbrs.read_file(filename).split('\n')
    
    assert lines[0][:2] == '# '
    title = lines[0][2:]
    
    assert lines[1] == "'''"
    description = [ ]
    in_count = -1
    
    for i in lines[2:]:
        if i == "'''":
            break
        else:
            description.append(i)
            
            if in_count == -1:
                x = parse_digit(i)
                if x != -1:
                    in_count = x
    else:
        assert False
        
def parse_digit(x: str) -> int:
    x = [ i if i.isdigit() else ' ' for i in x ]
    return int(''.join(x).split()[0])

def get_case_input_dat_count(filename: str) -> int:
    '''only for external callers'''
    get_script_information(filename)
    return in_count

def str2unicode(s: str) -> str:
    s = ascii(s)
    s = list(s)
    s.pop()
    s.pop(0)
    
    return ''.join(s)

def check_and_filter_in_out_files_folder(files: list[str]) -> list[int]:
    assert len(files) % 2 == 0 # in pairs
    out = [ ]

    # check files format
    for i in files:
        parts = i.split('.')
        assert len(parts) == 2
        no, ext = parts

        assert no.isdigit()
        assert ext in [ 'in', 'out' ]

        if ext == 'in':
            assert f'{no}.out' in files
            out.append(no)
        else:
            assert ext == 'out' # double-check
            assert f'{no}.in' in files

    return out

def make_in_out_files_configuration(files: list[str], TEMPLATE: str) -> str:
    return ',\n'.join([ TEMPLATE.format(i) for i in
        check_and_filter_in_out_files_folder(files) ])

def make_test_case_conf(testcase_home: str) -> str:
    PROBLEM_JSON = 'problem.json'
    files = os.listdir(testcase_home)

    # drop problem.json if any
    assert files.count(PROBLEM_JSON) in [ 0, 1 ]
    if PROBLEM_JSON in files:
        files.remove(PROBLEM_JSON)

    # generate configuration
    return make_in_out_files_configuration(files, '''
    {{
        "score": 100,
        "input_name": "{0}.in",
        "output_name": "{0}.out"
    }}''')

def make_sample(sample_home: str) -> str:
    return make_in_out_files_configuration(os.listdir(sample_home), '''
    {{
        "input": "{}",
        "output": "{}"
    }}
    ''')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate problem.json.')
    parser.add_argument('filename')
    parser.add_argument('testcase_home')
    parser.add_argument('sample_home')
    args = parser.parse_args()

    get_script_information(args.filename)
    S1 = str2unicode('详见样例')

    print('''{
        "display_id": "%s",
        "title": "%s",
        "description": {
            "format": "html",
            "value": "<pre>%s</pre>"
        },
        "tags": [ "PP" ],
        "input_description": {
            "format": "html",
            "value": "<p>%s</p>"
        },
        "output_description": {
            "format": "html",
            "value": "<p>%s</p>"
        },
        "hint": { "format": "html", "value": "" },
        "time_limit": 1000,
        "memory_limit": 256,
        "template": {},
        "spj": null,
        "rule_type": "ACM",
        "source": "Python%s http://222.201.101.8",
        "answers": [],
        "test_case_score": [ %s ],
        "sample": [ %s ]
    }''' % ('PP-' + args.filename.split('.')[0], str2unicode(title),
            str2unicode('\n'.join(description)),
            S1, S1, str2unicode('刷题系统'),
            make_test_case_conf(args.testcase_home),
            make_sample(args.sample_home)))
