# py-online-judge-question-generator

See also: https://github.com/QingdaoU/OnlineJudge/blob/master/problem/models.py

##

## Old

Format:
- PP-000, PP-001, ... -> 02.语言元素
- PP-100, ... -> 03

```
ProblemSet.zip
|-1
    |–problem.json
    |–testcase
        |—1.in
        |—1.out
        |…
|-2
    |–problem.json
    |–testcase
        |—1.in
        |—1.out
        |…
|…
```

https://hub.fastgit.org/jackfrued/Python-100-Days/tree/master/Day01-15

Example output:

```Makefile
upload/1/testcase/1.in:
	./make_input.py 1 > upload/1/testcase/1.in

upload/1/testcase/1.out: upload/1/testcase/1.in
	python3 cases/200.py < upload/1/testcase/1.in > upload/1/testcase/1.out

upload/1/testcase/2.in:
	./make_input.py 1 > upload/1/testcase/2.in

upload/1/testcase/2.out: upload/1/testcase/2.in
	python3 cases/200.py < upload/1/testcase/2.in > upload/1/testcase/2.out

upload/1/testcase/3.in:
	./make_input.py 1 > upload/1/testcase/3.in

upload/1/testcase/3.out: upload/1/testcase/3.in
	python3 cases/200.py < upload/1/testcase/3.in > upload/1/testcase/3.out

upload/1/testcase/4.in:
	./make_input.py 1 > upload/1/testcase/4.in

upload/1/testcase/4.out: upload/1/testcase/4.in
	python3 cases/200.py < upload/1/testcase/4.in > upload/1/testcase/4.out

upload/1/testcase/5.in:
	./make_input.py 1 > upload/1/testcase/5.in

upload/1/testcase/5.out: upload/1/testcase/5.in
	python3 cases/200.py < upload/1/testcase/5.in > upload/1/testcase/5.out

sample/1/1.in:
	./make_input.py 1 > sample/1/1.in

sample/1/1.out: sample/1/1.in
	python3 cases/200.py < sample/1/1.in > sample/1/1.out

sample/1/2.in:
	./make_input.py 1 > sample/1/2.in

sample/1/2.out: sample/1/2.in
	python3 cases/200.py < sample/1/2.in > sample/1/2.out

sample/1/3.in:
	./make_input.py 1 > sample/1/3.in

sample/1/3.out: sample/1/3.in
	python3 cases/200.py < sample/1/3.in > sample/1/3.out

upload/1/problem.json:
	./make_problem_json.py cases/200.py upload/1/testcase sample/1 > upload/1/problem.json

pp200: upload/1/testcase/1.in upload/1/testcase/1.out upload/1/testcase/2.in upload/1/testcase/2.out upload/1/testcase/3.in upload/1/testcase/3.out upload/1/testcase/4.in upload/1/testcase/4.out upload/1/testcase/5.in upload/1/testcase/5.out sample/1/1.in sample/1/1.out sample/1/2.in sample/1/2.out sample/1/3.in sample/1/3.out upload/1/problem.json upload/1/problem.json


upload/2/testcase/1.in:
	./make_input.py 1 > upload/2/testcase/1.in

upload/2/testcase/1.out: upload/2/testcase/1.in
	python3 cases/201.py < upload/2/testcase/1.in > upload/2/testcase/1.out

upload/2/testcase/2.in:
	./make_input.py 1 > upload/2/testcase/2.in

upload/2/testcase/2.out: upload/2/testcase/2.in
	python3 cases/201.py < upload/2/testcase/2.in > upload/2/testcase/2.out

upload/2/testcase/3.in:
	./make_input.py 1 > upload/2/testcase/3.in

upload/2/testcase/3.out: upload/2/testcase/3.in
	python3 cases/201.py < upload/2/testcase/3.in > upload/2/testcase/3.out

upload/2/testcase/4.in:
	./make_input.py 1 > upload/2/testcase/4.in

upload/2/testcase/4.out: upload/2/testcase/4.in
	python3 cases/201.py < upload/2/testcase/4.in > upload/2/testcase/4.out

upload/2/testcase/5.in:
	./make_input.py 1 > upload/2/testcase/5.in

upload/2/testcase/5.out: upload/2/testcase/5.in
	python3 cases/201.py < upload/2/testcase/5.in > upload/2/testcase/5.out

sample/2/1.in:
	./make_input.py 1 > sample/2/1.in

sample/2/1.out: sample/2/1.in
	python3 cases/201.py < sample/2/1.in > sample/2/1.out

sample/2/2.in:
	./make_input.py 1 > sample/2/2.in

sample/2/2.out: sample/2/2.in
	python3 cases/201.py < sample/2/2.in > sample/2/2.out

sample/2/3.in:
	./make_input.py 1 > sample/2/3.in

sample/2/3.out: sample/2/3.in
	python3 cases/201.py < sample/2/3.in > sample/2/3.out

upload/2/problem.json:
	./make_problem_json.py cases/201.py upload/2/testcase sample/2 > upload/2/problem.json

pp201: upload/2/testcase/1.in upload/2/testcase/1.out upload/2/testcase/2.in upload/2/testcase/2.out upload/2/testcase/3.in upload/2/testcase/3.out upload/2/testcase/4.in upload/2/testcase/4.out upload/2/testcase/5.in upload/2/testcase/5.out sample/2/1.in sample/2/1.out sample/2/2.in sample/2/2.out sample/2/3.in sample/2/3.out upload/2/problem.json upload/2/problem.json


upload/3/testcase/1.in:
	./make_input.py 3 > upload/3/testcase/1.in

upload/3/testcase/1.out: upload/3/testcase/1.in
	python3 cases/102.py < upload/3/testcase/1.in > upload/3/testcase/1.out

upload/3/testcase/2.in:
	./make_input.py 3 > upload/3/testcase/2.in

upload/3/testcase/2.out: upload/3/testcase/2.in
	python3 cases/102.py < upload/3/testcase/2.in > upload/3/testcase/2.out

upload/3/testcase/3.in:
	./make_input.py 3 > upload/3/testcase/3.in

upload/3/testcase/3.out: upload/3/testcase/3.in
	python3 cases/102.py < upload/3/testcase/3.in > upload/3/testcase/3.out

upload/3/testcase/4.in:
	./make_input.py 3 > upload/3/testcase/4.in

upload/3/testcase/4.out: upload/3/testcase/4.in
	python3 cases/102.py < upload/3/testcase/4.in > upload/3/testcase/4.out

upload/3/testcase/5.in:
	./make_input.py 3 > upload/3/testcase/5.in

upload/3/testcase/5.out: upload/3/testcase/5.in
	python3 cases/102.py < upload/3/testcase/5.in > upload/3/testcase/5.out

sample/3/1.in:
	./make_input.py 3 > sample/3/1.in

sample/3/1.out: sample/3/1.in
	python3 cases/102.py < sample/3/1.in > sample/3/1.out

sample/3/2.in:
	./make_input.py 3 > sample/3/2.in

sample/3/2.out: sample/3/2.in
	python3 cases/102.py < sample/3/2.in > sample/3/2.out

sample/3/3.in:
	./make_input.py 3 > sample/3/3.in

sample/3/3.out: sample/3/3.in
	python3 cases/102.py < sample/3/3.in > sample/3/3.out

upload/3/problem.json:
	./make_problem_json.py cases/102.py upload/3/testcase sample/3 > upload/3/problem.json

pp102: upload/3/testcase/1.in upload/3/testcase/1.out upload/3/testcase/2.in upload/3/testcase/2.out upload/3/testcase/3.in upload/3/testcase/3.out upload/3/testcase/4.in upload/3/testcase/4.out upload/3/testcase/5.in upload/3/testcase/5.out sample/3/1.in sample/3/1.out sample/3/2.in sample/3/2.out sample/3/3.in sample/3/3.out upload/3/problem.json upload/3/problem.json


upload/4/testcase/1.in:
	./make_input.py 1 > upload/4/testcase/1.in

upload/4/testcase/1.out: upload/4/testcase/1.in
	python3 cases/004.py < upload/4/testcase/1.in > upload/4/testcase/1.out

upload/4/testcase/2.in:
	./make_input.py 1 > upload/4/testcase/2.in

upload/4/testcase/2.out: upload/4/testcase/2.in
	python3 cases/004.py < upload/4/testcase/2.in > upload/4/testcase/2.out

upload/4/testcase/3.in:
	./make_input.py 1 > upload/4/testcase/3.in

upload/4/testcase/3.out: upload/4/testcase/3.in
	python3 cases/004.py < upload/4/testcase/3.in > upload/4/testcase/3.out

upload/4/testcase/4.in:
	./make_input.py 1 > upload/4/testcase/4.in

upload/4/testcase/4.out: upload/4/testcase/4.in
	python3 cases/004.py < upload/4/testcase/4.in > upload/4/testcase/4.out

upload/4/testcase/5.in:
	./make_input.py 1 > upload/4/testcase/5.in

upload/4/testcase/5.out: upload/4/testcase/5.in
	python3 cases/004.py < upload/4/testcase/5.in > upload/4/testcase/5.out

sample/4/1.in:
	./make_input.py 1 > sample/4/1.in

sample/4/1.out: sample/4/1.in
	python3 cases/004.py < sample/4/1.in > sample/4/1.out

sample/4/2.in:
	./make_input.py 1 > sample/4/2.in

sample/4/2.out: sample/4/2.in
	python3 cases/004.py < sample/4/2.in > sample/4/2.out

sample/4/3.in:
	./make_input.py 1 > sample/4/3.in

sample/4/3.out: sample/4/3.in
	python3 cases/004.py < sample/4/3.in > sample/4/3.out

upload/4/problem.json:
	./make_problem_json.py cases/004.py upload/4/testcase sample/4 > upload/4/problem.json

pp004: upload/4/testcase/1.in upload/4/testcase/1.out upload/4/testcase/2.in upload/4/testcase/2.out upload/4/testcase/3.in upload/4/testcase/3.out upload/4/testcase/4.in upload/4/testcase/4.out upload/4/testcase/5.in upload/4/testcase/5.out sample/4/1.in sample/4/1.out sample/4/2.in sample/4/2.out sample/4/3.in sample/4/3.out upload/4/problem.json upload/4/problem.json


upload/5/testcase/1.in:
	./make_input.py 8 > upload/5/testcase/1.in

upload/5/testcase/1.out: upload/5/testcase/1.in
	python3 cases/002.py < upload/5/testcase/1.in > upload/5/testcase/1.out

upload/5/testcase/2.in:
	./make_input.py 8 > upload/5/testcase/2.in

upload/5/testcase/2.out: upload/5/testcase/2.in
	python3 cases/002.py < upload/5/testcase/2.in > upload/5/testcase/2.out

upload/5/testcase/3.in:
	./make_input.py 8 > upload/5/testcase/3.in

upload/5/testcase/3.out: upload/5/testcase/3.in
	python3 cases/002.py < upload/5/testcase/3.in > upload/5/testcase/3.out

upload/5/testcase/4.in:
	./make_input.py 8 > upload/5/testcase/4.in

upload/5/testcase/4.out: upload/5/testcase/4.in
	python3 cases/002.py < upload/5/testcase/4.in > upload/5/testcase/4.out

upload/5/testcase/5.in:
	./make_input.py 8 > upload/5/testcase/5.in

upload/5/testcase/5.out: upload/5/testcase/5.in
	python3 cases/002.py < upload/5/testcase/5.in > upload/5/testcase/5.out

sample/5/1.in:
	./make_input.py 8 > sample/5/1.in

sample/5/1.out: sample/5/1.in
	python3 cases/002.py < sample/5/1.in > sample/5/1.out

sample/5/2.in:
	./make_input.py 8 > sample/5/2.in

sample/5/2.out: sample/5/2.in
	python3 cases/002.py < sample/5/2.in > sample/5/2.out

sample/5/3.in:
	./make_input.py 8 > sample/5/3.in

sample/5/3.out: sample/5/3.in
	python3 cases/002.py < sample/5/3.in > sample/5/3.out

upload/5/problem.json:
	./make_problem_json.py cases/002.py upload/5/testcase sample/5 > upload/5/problem.json

pp002: upload/5/testcase/1.in upload/5/testcase/1.out upload/5/testcase/2.in upload/5/testcase/2.out upload/5/testcase/3.in upload/5/testcase/3.out upload/5/testcase/4.in upload/5/testcase/4.out upload/5/testcase/5.in upload/5/testcase/5.out sample/5/1.in sample/5/1.out sample/5/2.in sample/5/2.out sample/5/3.in sample/5/3.out upload/5/problem.json upload/5/problem.json


upload/6/testcase/1.in:
	./make_input.py 1 > upload/6/testcase/1.in

upload/6/testcase/1.out: upload/6/testcase/1.in
	python3 cases/005.py < upload/6/testcase/1.in > upload/6/testcase/1.out

upload/6/testcase/2.in:
	./make_input.py 1 > upload/6/testcase/2.in

upload/6/testcase/2.out: upload/6/testcase/2.in
	python3 cases/005.py < upload/6/testcase/2.in > upload/6/testcase/2.out

upload/6/testcase/3.in:
	./make_input.py 1 > upload/6/testcase/3.in

upload/6/testcase/3.out: upload/6/testcase/3.in
	python3 cases/005.py < upload/6/testcase/3.in > upload/6/testcase/3.out

upload/6/testcase/4.in:
	./make_input.py 1 > upload/6/testcase/4.in

upload/6/testcase/4.out: upload/6/testcase/4.in
	python3 cases/005.py < upload/6/testcase/4.in > upload/6/testcase/4.out

upload/6/testcase/5.in:
	./make_input.py 1 > upload/6/testcase/5.in

upload/6/testcase/5.out: upload/6/testcase/5.in
	python3 cases/005.py < upload/6/testcase/5.in > upload/6/testcase/5.out

sample/6/1.in:
	./make_input.py 1 > sample/6/1.in

sample/6/1.out: sample/6/1.in
	python3 cases/005.py < sample/6/1.in > sample/6/1.out

sample/6/2.in:
	./make_input.py 1 > sample/6/2.in

sample/6/2.out: sample/6/2.in
	python3 cases/005.py < sample/6/2.in > sample/6/2.out

sample/6/3.in:
	./make_input.py 1 > sample/6/3.in

sample/6/3.out: sample/6/3.in
	python3 cases/005.py < sample/6/3.in > sample/6/3.out

upload/6/problem.json:
	./make_problem_json.py cases/005.py upload/6/testcase sample/6 > upload/6/problem.json

pp005: upload/6/testcase/1.in upload/6/testcase/1.out upload/6/testcase/2.in upload/6/testcase/2.out upload/6/testcase/3.in upload/6/testcase/3.out upload/6/testcase/4.in upload/6/testcase/4.out upload/6/testcase/5.in upload/6/testcase/5.out sample/6/1.in sample/6/1.out sample/6/2.in sample/6/2.out sample/6/3.in sample/6/3.out upload/6/problem.json upload/6/problem.json


upload/7/testcase/1.in:
	./make_input.py 1 > upload/7/testcase/1.in

upload/7/testcase/1.out: upload/7/testcase/1.in
	python3 cases/100.py < upload/7/testcase/1.in > upload/7/testcase/1.out

upload/7/testcase/2.in:
	./make_input.py 1 > upload/7/testcase/2.in

upload/7/testcase/2.out: upload/7/testcase/2.in
	python3 cases/100.py < upload/7/testcase/2.in > upload/7/testcase/2.out

upload/7/testcase/3.in:
	./make_input.py 1 > upload/7/testcase/3.in

upload/7/testcase/3.out: upload/7/testcase/3.in
	python3 cases/100.py < upload/7/testcase/3.in > upload/7/testcase/3.out

upload/7/testcase/4.in:
	./make_input.py 1 > upload/7/testcase/4.in

upload/7/testcase/4.out: upload/7/testcase/4.in
	python3 cases/100.py < upload/7/testcase/4.in > upload/7/testcase/4.out

upload/7/testcase/5.in:
	./make_input.py 1 > upload/7/testcase/5.in

upload/7/testcase/5.out: upload/7/testcase/5.in
	python3 cases/100.py < upload/7/testcase/5.in > upload/7/testcase/5.out

sample/7/1.in:
	./make_input.py 1 > sample/7/1.in

sample/7/1.out: sample/7/1.in
	python3 cases/100.py < sample/7/1.in > sample/7/1.out

sample/7/2.in:
	./make_input.py 1 > sample/7/2.in

sample/7/2.out: sample/7/2.in
	python3 cases/100.py < sample/7/2.in > sample/7/2.out

sample/7/3.in:
	./make_input.py 1 > sample/7/3.in

sample/7/3.out: sample/7/3.in
	python3 cases/100.py < sample/7/3.in > sample/7/3.out

upload/7/problem.json:
	./make_problem_json.py cases/100.py upload/7/testcase sample/7 > upload/7/problem.json

pp100: upload/7/testcase/1.in upload/7/testcase/1.out upload/7/testcase/2.in upload/7/testcase/2.out upload/7/testcase/3.in upload/7/testcase/3.out upload/7/testcase/4.in upload/7/testcase/4.out upload/7/testcase/5.in upload/7/testcase/5.out sample/7/1.in sample/7/1.out sample/7/2.in sample/7/2.out sample/7/3.in sample/7/3.out upload/7/problem.json upload/7/problem.json


upload/8/testcase/1.in:
	./make_input.py 1 > upload/8/testcase/1.in

upload/8/testcase/1.out: upload/8/testcase/1.in
	python3 cases/003.py < upload/8/testcase/1.in > upload/8/testcase/1.out

upload/8/testcase/2.in:
	./make_input.py 1 > upload/8/testcase/2.in

upload/8/testcase/2.out: upload/8/testcase/2.in
	python3 cases/003.py < upload/8/testcase/2.in > upload/8/testcase/2.out

upload/8/testcase/3.in:
	./make_input.py 1 > upload/8/testcase/3.in

upload/8/testcase/3.out: upload/8/testcase/3.in
	python3 cases/003.py < upload/8/testcase/3.in > upload/8/testcase/3.out

upload/8/testcase/4.in:
	./make_input.py 1 > upload/8/testcase/4.in

upload/8/testcase/4.out: upload/8/testcase/4.in
	python3 cases/003.py < upload/8/testcase/4.in > upload/8/testcase/4.out

upload/8/testcase/5.in:
	./make_input.py 1 > upload/8/testcase/5.in

upload/8/testcase/5.out: upload/8/testcase/5.in
	python3 cases/003.py < upload/8/testcase/5.in > upload/8/testcase/5.out

sample/8/1.in:
	./make_input.py 1 > sample/8/1.in

sample/8/1.out: sample/8/1.in
	python3 cases/003.py < sample/8/1.in > sample/8/1.out

sample/8/2.in:
	./make_input.py 1 > sample/8/2.in

sample/8/2.out: sample/8/2.in
	python3 cases/003.py < sample/8/2.in > sample/8/2.out

sample/8/3.in:
	./make_input.py 1 > sample/8/3.in

sample/8/3.out: sample/8/3.in
	python3 cases/003.py < sample/8/3.in > sample/8/3.out

upload/8/problem.json:
	./make_problem_json.py cases/003.py upload/8/testcase sample/8 > upload/8/problem.json

pp003: upload/8/testcase/1.in upload/8/testcase/1.out upload/8/testcase/2.in upload/8/testcase/2.out upload/8/testcase/3.in upload/8/testcase/3.out upload/8/testcase/4.in upload/8/testcase/4.out upload/8/testcase/5.in upload/8/testcase/5.out sample/8/1.in sample/8/1.out sample/8/2.in sample/8/2.out sample/8/3.in sample/8/3.out upload/8/problem.json upload/8/problem.json


upload/9/testcase/1.in:
	./make_input.py 1 > upload/9/testcase/1.in

upload/9/testcase/1.out: upload/9/testcase/1.in
	python3 cases/101.py < upload/9/testcase/1.in > upload/9/testcase/1.out

upload/9/testcase/2.in:
	./make_input.py 1 > upload/9/testcase/2.in

upload/9/testcase/2.out: upload/9/testcase/2.in
	python3 cases/101.py < upload/9/testcase/2.in > upload/9/testcase/2.out

upload/9/testcase/3.in:
	./make_input.py 1 > upload/9/testcase/3.in

upload/9/testcase/3.out: upload/9/testcase/3.in
	python3 cases/101.py < upload/9/testcase/3.in > upload/9/testcase/3.out

upload/9/testcase/4.in:
	./make_input.py 1 > upload/9/testcase/4.in

upload/9/testcase/4.out: upload/9/testcase/4.in
	python3 cases/101.py < upload/9/testcase/4.in > upload/9/testcase/4.out

upload/9/testcase/5.in:
	./make_input.py 1 > upload/9/testcase/5.in

upload/9/testcase/5.out: upload/9/testcase/5.in
	python3 cases/101.py < upload/9/testcase/5.in > upload/9/testcase/5.out

sample/9/1.in:
	./make_input.py 1 > sample/9/1.in

sample/9/1.out: sample/9/1.in
	python3 cases/101.py < sample/9/1.in > sample/9/1.out

sample/9/2.in:
	./make_input.py 1 > sample/9/2.in

sample/9/2.out: sample/9/2.in
	python3 cases/101.py < sample/9/2.in > sample/9/2.out

sample/9/3.in:
	./make_input.py 1 > sample/9/3.in

sample/9/3.out: sample/9/3.in
	python3 cases/101.py < sample/9/3.in > sample/9/3.out

upload/9/problem.json:
	./make_problem_json.py cases/101.py upload/9/testcase sample/9 > upload/9/problem.json

pp101: upload/9/testcase/1.in upload/9/testcase/1.out upload/9/testcase/2.in upload/9/testcase/2.out upload/9/testcase/3.in upload/9/testcase/3.out upload/9/testcase/4.in upload/9/testcase/4.out upload/9/testcase/5.in upload/9/testcase/5.out sample/9/1.in sample/9/1.out sample/9/2.in sample/9/2.out sample/9/3.in sample/9/3.out upload/9/problem.json upload/9/problem.json


upload/10/testcase/1.in:
	./make_input.py 1 > upload/10/testcase/1.in

upload/10/testcase/1.out: upload/10/testcase/1.in
	python3 cases/202.py < upload/10/testcase/1.in > upload/10/testcase/1.out

upload/10/testcase/2.in:
	./make_input.py 1 > upload/10/testcase/2.in

upload/10/testcase/2.out: upload/10/testcase/2.in
	python3 cases/202.py < upload/10/testcase/2.in > upload/10/testcase/2.out

upload/10/testcase/3.in:
	./make_input.py 1 > upload/10/testcase/3.in

upload/10/testcase/3.out: upload/10/testcase/3.in
	python3 cases/202.py < upload/10/testcase/3.in > upload/10/testcase/3.out

upload/10/testcase/4.in:
	./make_input.py 1 > upload/10/testcase/4.in

upload/10/testcase/4.out: upload/10/testcase/4.in
	python3 cases/202.py < upload/10/testcase/4.in > upload/10/testcase/4.out

upload/10/testcase/5.in:
	./make_input.py 1 > upload/10/testcase/5.in

upload/10/testcase/5.out: upload/10/testcase/5.in
	python3 cases/202.py < upload/10/testcase/5.in > upload/10/testcase/5.out

sample/10/1.in:
	./make_input.py 1 > sample/10/1.in

sample/10/1.out: sample/10/1.in
	python3 cases/202.py < sample/10/1.in > sample/10/1.out

sample/10/2.in:
	./make_input.py 1 > sample/10/2.in

sample/10/2.out: sample/10/2.in
	python3 cases/202.py < sample/10/2.in > sample/10/2.out

sample/10/3.in:
	./make_input.py 1 > sample/10/3.in

sample/10/3.out: sample/10/3.in
	python3 cases/202.py < sample/10/3.in > sample/10/3.out

upload/10/problem.json:
	./make_problem_json.py cases/202.py upload/10/testcase sample/10 > upload/10/problem.json

pp202: upload/10/testcase/1.in upload/10/testcase/1.out upload/10/testcase/2.in upload/10/testcase/2.out upload/10/testcase/3.in upload/10/testcase/3.out upload/10/testcase/4.in upload/10/testcase/4.out upload/10/testcase/5.in upload/10/testcase/5.out sample/10/1.in sample/10/1.out sample/10/2.in sample/10/2.out sample/10/3.in sample/10/3.out upload/10/problem.json upload/10/problem.json


upload/11/testcase/1.in:
	./make_input.py 2 > upload/11/testcase/1.in

upload/11/testcase/1.out: upload/11/testcase/1.in
	python3 cases/204.py < upload/11/testcase/1.in > upload/11/testcase/1.out

upload/11/testcase/2.in:
	./make_input.py 2 > upload/11/testcase/2.in

upload/11/testcase/2.out: upload/11/testcase/2.in
	python3 cases/204.py < upload/11/testcase/2.in > upload/11/testcase/2.out

upload/11/testcase/3.in:
	./make_input.py 2 > upload/11/testcase/3.in

upload/11/testcase/3.out: upload/11/testcase/3.in
	python3 cases/204.py < upload/11/testcase/3.in > upload/11/testcase/3.out

upload/11/testcase/4.in:
	./make_input.py 2 > upload/11/testcase/4.in

upload/11/testcase/4.out: upload/11/testcase/4.in
	python3 cases/204.py < upload/11/testcase/4.in > upload/11/testcase/4.out

upload/11/testcase/5.in:
	./make_input.py 2 > upload/11/testcase/5.in

upload/11/testcase/5.out: upload/11/testcase/5.in
	python3 cases/204.py < upload/11/testcase/5.in > upload/11/testcase/5.out

sample/11/1.in:
	./make_input.py 2 > sample/11/1.in

sample/11/1.out: sample/11/1.in
	python3 cases/204.py < sample/11/1.in > sample/11/1.out

sample/11/2.in:
	./make_input.py 2 > sample/11/2.in

sample/11/2.out: sample/11/2.in
	python3 cases/204.py < sample/11/2.in > sample/11/2.out

sample/11/3.in:
	./make_input.py 2 > sample/11/3.in

sample/11/3.out: sample/11/3.in
	python3 cases/204.py < sample/11/3.in > sample/11/3.out

upload/11/problem.json:
	./make_problem_json.py cases/204.py upload/11/testcase sample/11 > upload/11/problem.json

pp204: upload/11/testcase/1.in upload/11/testcase/1.out upload/11/testcase/2.in upload/11/testcase/2.out upload/11/testcase/3.in upload/11/testcase/3.out upload/11/testcase/4.in upload/11/testcase/4.out upload/11/testcase/5.in upload/11/testcase/5.out sample/11/1.in sample/11/1.out sample/11/2.in sample/11/2.out sample/11/3.in sample/11/3.out upload/11/problem.json upload/11/problem.json


upload/12/testcase/1.in:
	./make_input.py 1 > upload/12/testcase/1.in

upload/12/testcase/1.out: upload/12/testcase/1.in
	python3 cases/203.py < upload/12/testcase/1.in > upload/12/testcase/1.out

upload/12/testcase/2.in:
	./make_input.py 1 > upload/12/testcase/2.in

upload/12/testcase/2.out: upload/12/testcase/2.in
	python3 cases/203.py < upload/12/testcase/2.in > upload/12/testcase/2.out

upload/12/testcase/3.in:
	./make_input.py 1 > upload/12/testcase/3.in

upload/12/testcase/3.out: upload/12/testcase/3.in
	python3 cases/203.py < upload/12/testcase/3.in > upload/12/testcase/3.out

upload/12/testcase/4.in:
	./make_input.py 1 > upload/12/testcase/4.in

upload/12/testcase/4.out: upload/12/testcase/4.in
	python3 cases/203.py < upload/12/testcase/4.in > upload/12/testcase/4.out

upload/12/testcase/5.in:
	./make_input.py 1 > upload/12/testcase/5.in

upload/12/testcase/5.out: upload/12/testcase/5.in
	python3 cases/203.py < upload/12/testcase/5.in > upload/12/testcase/5.out

sample/12/1.in:
	./make_input.py 1 > sample/12/1.in

sample/12/1.out: sample/12/1.in
	python3 cases/203.py < sample/12/1.in > sample/12/1.out

sample/12/2.in:
	./make_input.py 1 > sample/12/2.in

sample/12/2.out: sample/12/2.in
	python3 cases/203.py < sample/12/2.in > sample/12/2.out

sample/12/3.in:
	./make_input.py 1 > sample/12/3.in

sample/12/3.out: sample/12/3.in
	python3 cases/203.py < sample/12/3.in > sample/12/3.out

upload/12/problem.json:
	./make_problem_json.py cases/203.py upload/12/testcase sample/12 > upload/12/problem.json

pp203: upload/12/testcase/1.in upload/12/testcase/1.out upload/12/testcase/2.in upload/12/testcase/2.out upload/12/testcase/3.in upload/12/testcase/3.out upload/12/testcase/4.in upload/12/testcase/4.out upload/12/testcase/5.in upload/12/testcase/5.out sample/12/1.in sample/12/1.out sample/12/2.in sample/12/2.out sample/12/3.in sample/12/3.out upload/12/problem.json upload/12/problem.json


all: prepare_dir pp200 pp201 pp102 pp004 pp002 pp005 pp100 pp003 pp101 pp202 pp204 pp203


prepare_dir:
	mkdir -p upload/1
	mkdir -p upload/1/testcase/
	mkdir -p sample/1
	mkdir -p upload/2
	mkdir -p upload/2/testcase/
	mkdir -p sample/2
	mkdir -p upload/3
	mkdir -p upload/3/testcase/
	mkdir -p sample/3
	mkdir -p upload/4
	mkdir -p upload/4/testcase/
	mkdir -p sample/4
	mkdir -p upload/5
	mkdir -p upload/5/testcase/
	mkdir -p sample/5
	mkdir -p upload/6
	mkdir -p upload/6/testcase/
	mkdir -p sample/6
	mkdir -p upload/7
	mkdir -p upload/7/testcase/
	mkdir -p sample/7
	mkdir -p upload/8
	mkdir -p upload/8/testcase/
	mkdir -p sample/8
	mkdir -p upload/9
	mkdir -p upload/9/testcase/
	mkdir -p sample/9
	mkdir -p upload/10
	mkdir -p upload/10/testcase/
	mkdir -p sample/10
	mkdir -p upload/11
	mkdir -p upload/11/testcase/
	mkdir -p sample/11
	mkdir -p upload/12
	mkdir -p upload/12/testcase/
	mkdir -p sample/12
```

Building:

```shell
$ ./make.py > Makefile
$ make all
mkdir -p upload/1
mkdir -p upload/1/testcase/
mkdir -p sample/1
mkdir -p upload/2
mkdir -p upload/2/testcase/
mkdir -p sample/2
mkdir -p upload/3
mkdir -p upload/3/testcase/
mkdir -p sample/3
mkdir -p upload/4
mkdir -p upload/4/testcase/
mkdir -p sample/4
mkdir -p upload/5
mkdir -p upload/5/testcase/
mkdir -p sample/5
mkdir -p upload/6
mkdir -p upload/6/testcase/
mkdir -p sample/6
mkdir -p upload/7
mkdir -p upload/7/testcase/
mkdir -p sample/7
mkdir -p upload/8
mkdir -p upload/8/testcase/
mkdir -p sample/8
mkdir -p upload/9
mkdir -p upload/9/testcase/
mkdir -p sample/9
mkdir -p upload/10
mkdir -p upload/10/testcase/
mkdir -p sample/10
mkdir -p upload/11
mkdir -p upload/11/testcase/
mkdir -p sample/11
mkdir -p upload/12
mkdir -p upload/12/testcase/
mkdir -p sample/12
./make_input.py 1 > upload/1/testcase/1.in
python3 cases/200.py < upload/1/testcase/1.in > upload/1/testcase/1.out
./make_input.py 1 > upload/1/testcase/2.in
python3 cases/200.py < upload/1/testcase/2.in > upload/1/testcase/2.out
./make_input.py 1 > upload/1/testcase/3.in
python3 cases/200.py < upload/1/testcase/3.in > upload/1/testcase/3.out
./make_input.py 1 > upload/1/testcase/4.in
python3 cases/200.py < upload/1/testcase/4.in > upload/1/testcase/4.out
./make_input.py 1 > upload/1/testcase/5.in
python3 cases/200.py < upload/1/testcase/5.in > upload/1/testcase/5.out
./make_problem_json.py cases/200.py upload/1/testcase sample/1 > upload/1/problem.json
./make_input.py 1 > upload/2/testcase/1.in
python3 cases/201.py < upload/2/testcase/1.in > upload/2/testcase/1.out
./make_input.py 1 > upload/2/testcase/2.in
python3 cases/201.py < upload/2/testcase/2.in > upload/2/testcase/2.out
./make_input.py 1 > upload/2/testcase/3.in
python3 cases/201.py < upload/2/testcase/3.in > upload/2/testcase/3.out
./make_input.py 1 > upload/2/testcase/4.in
python3 cases/201.py < upload/2/testcase/4.in > upload/2/testcase/4.out
./make_input.py 1 > upload/2/testcase/5.in
python3 cases/201.py < upload/2/testcase/5.in > upload/2/testcase/5.out
./make_problem_json.py cases/201.py upload/2/testcase sample/2 > upload/2/problem.json
./make_input.py 3 > upload/3/testcase/1.in
python3 cases/102.py < upload/3/testcase/1.in > upload/3/testcase/1.out
./make_input.py 3 > upload/3/testcase/2.in
python3 cases/102.py < upload/3/testcase/2.in > upload/3/testcase/2.out
./make_input.py 3 > upload/3/testcase/3.in
python3 cases/102.py < upload/3/testcase/3.in > upload/3/testcase/3.out
./make_input.py 3 > upload/3/testcase/4.in
python3 cases/102.py < upload/3/testcase/4.in > upload/3/testcase/4.out
./make_input.py 3 > upload/3/testcase/5.in
python3 cases/102.py < upload/3/testcase/5.in > upload/3/testcase/5.out
./make_problem_json.py cases/102.py upload/3/testcase sample/3 > upload/3/problem.json
./make_input.py 1 > upload/4/testcase/1.in
python3 cases/004.py < upload/4/testcase/1.in > upload/4/testcase/1.out
./make_input.py 1 > upload/4/testcase/2.in
python3 cases/004.py < upload/4/testcase/2.in > upload/4/testcase/2.out
./make_input.py 1 > upload/4/testcase/3.in
python3 cases/004.py < upload/4/testcase/3.in > upload/4/testcase/3.out
./make_input.py 1 > upload/4/testcase/4.in
python3 cases/004.py < upload/4/testcase/4.in > upload/4/testcase/4.out
./make_input.py 1 > upload/4/testcase/5.in
python3 cases/004.py < upload/4/testcase/5.in > upload/4/testcase/5.out
./make_problem_json.py cases/004.py upload/4/testcase sample/4 > upload/4/problem.json
./make_input.py 8 > upload/5/testcase/1.in
python3 cases/002.py < upload/5/testcase/1.in > upload/5/testcase/1.out
./make_input.py 8 > upload/5/testcase/2.in
python3 cases/002.py < upload/5/testcase/2.in > upload/5/testcase/2.out
./make_input.py 8 > upload/5/testcase/3.in
python3 cases/002.py < upload/5/testcase/3.in > upload/5/testcase/3.out
./make_input.py 8 > upload/5/testcase/4.in
python3 cases/002.py < upload/5/testcase/4.in > upload/5/testcase/4.out
./make_input.py 8 > upload/5/testcase/5.in
python3 cases/002.py < upload/5/testcase/5.in > upload/5/testcase/5.out
./make_problem_json.py cases/002.py upload/5/testcase sample/5 > upload/5/problem.json
./make_input.py 1 > upload/6/testcase/1.in
python3 cases/005.py < upload/6/testcase/1.in > upload/6/testcase/1.out
./make_input.py 1 > upload/6/testcase/2.in
python3 cases/005.py < upload/6/testcase/2.in > upload/6/testcase/2.out
./make_input.py 1 > upload/6/testcase/3.in
python3 cases/005.py < upload/6/testcase/3.in > upload/6/testcase/3.out
./make_input.py 1 > upload/6/testcase/4.in
python3 cases/005.py < upload/6/testcase/4.in > upload/6/testcase/4.out
./make_input.py 1 > upload/6/testcase/5.in
python3 cases/005.py < upload/6/testcase/5.in > upload/6/testcase/5.out
./make_problem_json.py cases/005.py upload/6/testcase sample/6 > upload/6/problem.json
./make_input.py 1 > upload/7/testcase/1.in
python3 cases/100.py < upload/7/testcase/1.in > upload/7/testcase/1.out
./make_input.py 1 > upload/7/testcase/2.in
python3 cases/100.py < upload/7/testcase/2.in > upload/7/testcase/2.out
./make_input.py 1 > upload/7/testcase/3.in
python3 cases/100.py < upload/7/testcase/3.in > upload/7/testcase/3.out
./make_input.py 1 > upload/7/testcase/4.in
python3 cases/100.py < upload/7/testcase/4.in > upload/7/testcase/4.out
./make_input.py 1 > upload/7/testcase/5.in
python3 cases/100.py < upload/7/testcase/5.in > upload/7/testcase/5.out
./make_problem_json.py cases/100.py upload/7/testcase sample/7 > upload/7/problem.json
./make_input.py 1 > upload/8/testcase/1.in
python3 cases/003.py < upload/8/testcase/1.in > upload/8/testcase/1.out
./make_input.py 1 > upload/8/testcase/2.in
python3 cases/003.py < upload/8/testcase/2.in > upload/8/testcase/2.out
./make_input.py 1 > upload/8/testcase/3.in
python3 cases/003.py < upload/8/testcase/3.in > upload/8/testcase/3.out
./make_input.py 1 > upload/8/testcase/4.in
python3 cases/003.py < upload/8/testcase/4.in > upload/8/testcase/4.out
./make_input.py 1 > upload/8/testcase/5.in
python3 cases/003.py < upload/8/testcase/5.in > upload/8/testcase/5.out
./make_problem_json.py cases/003.py upload/8/testcase sample/8 > upload/8/problem.json
./make_input.py 1 > upload/9/testcase/1.in
python3 cases/101.py < upload/9/testcase/1.in > upload/9/testcase/1.out
./make_input.py 1 > upload/9/testcase/2.in
python3 cases/101.py < upload/9/testcase/2.in > upload/9/testcase/2.out
./make_input.py 1 > upload/9/testcase/3.in
python3 cases/101.py < upload/9/testcase/3.in > upload/9/testcase/3.out
./make_input.py 1 > upload/9/testcase/4.in
python3 cases/101.py < upload/9/testcase/4.in > upload/9/testcase/4.out
./make_input.py 1 > upload/9/testcase/5.in
python3 cases/101.py < upload/9/testcase/5.in > upload/9/testcase/5.out
./make_problem_json.py cases/101.py upload/9/testcase sample/9 > upload/9/problem.json
./make_input.py 1 > upload/10/testcase/1.in
python3 cases/202.py < upload/10/testcase/1.in > upload/10/testcase/1.out
./make_input.py 1 > upload/10/testcase/2.in
python3 cases/202.py < upload/10/testcase/2.in > upload/10/testcase/2.out
./make_input.py 1 > upload/10/testcase/3.in
python3 cases/202.py < upload/10/testcase/3.in > upload/10/testcase/3.out
./make_input.py 1 > upload/10/testcase/4.in
python3 cases/202.py < upload/10/testcase/4.in > upload/10/testcase/4.out
./make_input.py 1 > upload/10/testcase/5.in
python3 cases/202.py < upload/10/testcase/5.in > upload/10/testcase/5.out
./make_input.py 1 > sample/10/1.in
python3 cases/202.py < sample/10/1.in > sample/10/1.out
./make_input.py 1 > sample/10/2.in
python3 cases/202.py < sample/10/2.in > sample/10/2.out
./make_input.py 1 > sample/10/3.in
python3 cases/202.py < sample/10/3.in > sample/10/3.out
./make_problem_json.py cases/202.py upload/10/testcase sample/10 > upload/10/problem.json
./make_input.py 2 > upload/11/testcase/1.in
python3 cases/204.py < upload/11/testcase/1.in > upload/11/testcase/1.out
./make_input.py 2 > upload/11/testcase/2.in
python3 cases/204.py < upload/11/testcase/2.in > upload/11/testcase/2.out
./make_input.py 2 > upload/11/testcase/3.in
python3 cases/204.py < upload/11/testcase/3.in > upload/11/testcase/3.out
./make_input.py 2 > upload/11/testcase/4.in
python3 cases/204.py < upload/11/testcase/4.in > upload/11/testcase/4.out
./make_input.py 2 > upload/11/testcase/5.in
python3 cases/204.py < upload/11/testcase/5.in > upload/11/testcase/5.out
./make_input.py 2 > sample/11/1.in
python3 cases/204.py < sample/11/1.in > sample/11/1.out
./make_input.py 2 > sample/11/2.in
python3 cases/204.py < sample/11/2.in > sample/11/2.out
./make_input.py 2 > sample/11/3.in
python3 cases/204.py < sample/11/3.in > sample/11/3.out
./make_problem_json.py cases/204.py upload/11/testcase sample/11 > upload/11/problem.json
./make_input.py 1 > upload/12/testcase/1.in
python3 cases/203.py < upload/12/testcase/1.in > upload/12/testcase/1.out
./make_input.py 1 > upload/12/testcase/2.in
python3 cases/203.py < upload/12/testcase/2.in > upload/12/testcase/2.out
./make_input.py 1 > upload/12/testcase/3.in
python3 cases/203.py < upload/12/testcase/3.in > upload/12/testcase/3.out
./make_input.py 1 > upload/12/testcase/4.in
python3 cases/203.py < upload/12/testcase/4.in > upload/12/testcase/4.out
./make_input.py 1 > upload/12/testcase/5.in
python3 cases/203.py < upload/12/testcase/5.in > upload/12/testcase/5.out
./make_input.py 1 > sample/12/1.in
python3 cases/203.py < sample/12/1.in > sample/12/1.out
./make_input.py 1 > sample/12/2.in
python3 cases/203.py < sample/12/2.in > sample/12/2.out
./make_input.py 1 > sample/12/3.in
python3 cases/203.py < sample/12/3.in > sample/12/3.out
./make_problem_json.py cases/203.py upload/12/testcase sample/12 > upload/12/problem.json
```

Finally packaging:

```
$ zip -r upload upload
updating: upload/ (stored 0%)
updating: upload/1/ (stored 0%)
updating: upload/1/testcase/ (stored 0%)
updating: upload/1/testcase/2.in (stored 0%)
updating: upload/1/testcase/1.out (stored 0%)
updating: upload/1/testcase/3.out (stored 0%)
updating: upload/1/testcase/1.in (stored 0%)
updating: upload/1/testcase/4.in (stored 0%)
updating: upload/1/testcase/5.in (stored 0%)
updating: upload/1/testcase/3.in (stored 0%)
updating: upload/1/testcase/2.out (stored 0%)
updating: upload/1/testcase/5.out (stored 0%)
updating: upload/1/testcase/4.out (stored 0%)
updating: upload/1/problem.json (deflated 71%)
  adding: upload/10/ (stored 0%)
  adding: upload/10/testcase/ (stored 0%)
  adding: upload/10/testcase/2.in (stored 0%)
  adding: upload/10/testcase/1.out (deflated 58%)
  adding: upload/10/testcase/3.out (deflated 58%)
  adding: upload/10/testcase/1.in (stored 0%)
  adding: upload/10/testcase/4.in (stored 0%)
  adding: upload/10/testcase/5.in (stored 0%)
  adding: upload/10/testcase/3.in (stored 0%)
  adding: upload/10/testcase/2.out (deflated 58%)
  adding: upload/10/testcase/5.out (deflated 58%)
  adding: upload/10/testcase/4.out (deflated 58%)
  adding: upload/10/problem.json (deflated 71%)
  adding: upload/6/ (stored 0%)
  adding: upload/6/testcase/ (stored 0%)
  adding: upload/6/testcase/2.in (stored 0%)
  adding: upload/6/testcase/1.out (stored 0%)
  adding: upload/6/testcase/3.out (stored 0%)
  adding: upload/6/testcase/1.in (stored 0%)
  adding: upload/6/testcase/4.in (stored 0%)
  adding: upload/6/testcase/5.in (stored 0%)
  adding: upload/6/testcase/3.in (stored 0%)
  adding: upload/6/testcase/2.out (stored 0%)
  adding: upload/6/testcase/5.out (stored 0%)
  adding: upload/6/testcase/4.out (stored 0%)
  adding: upload/6/problem.json (deflated 72%)
  adding: upload/4/ (stored 0%)
  adding: upload/4/testcase/ (stored 0%)
  adding: upload/4/testcase/2.in (stored 0%)
  adding: upload/4/testcase/1.out (stored 0%)
  adding: upload/4/testcase/3.out (stored 0%)
  adding: upload/4/testcase/1.in (stored 0%)
  adding: upload/4/testcase/4.in (stored 0%)
  adding: upload/4/testcase/5.in (stored 0%)
  adding: upload/4/testcase/3.in (stored 0%)
  adding: upload/4/testcase/2.out (stored 0%)
  adding: upload/4/testcase/5.out (stored 0%)
  adding: upload/4/testcase/4.out (stored 0%)
  adding: upload/4/problem.json (deflated 71%)
  adding: upload/5/ (stored 0%)
  adding: upload/5/testcase/ (stored 0%)
  adding: upload/5/testcase/2.in (deflated 5%)
  adding: upload/5/testcase/1.out (deflated 27%)
  adding: upload/5/testcase/3.out (deflated 54%)
  adding: upload/5/testcase/1.in (deflated 8%)
  adding: upload/5/testcase/4.in (deflated 5%)
  adding: upload/5/testcase/5.in (deflated 8%)
  adding: upload/5/testcase/3.in (deflated 5%)
  adding: upload/5/testcase/2.out (deflated 30%)
  adding: upload/5/testcase/5.out (deflated 27%)
  adding: upload/5/testcase/4.out (deflated 22%)
  adding: upload/5/problem.json (deflated 69%)
  adding: upload/12/ (stored 0%)
  adding: upload/12/testcase/ (stored 0%)
  adding: upload/12/testcase/2.in (stored 0%)
  adding: upload/12/testcase/1.out (stored 0%)
  adding: upload/12/testcase/3.out (stored 0%)
  adding: upload/12/testcase/1.in (stored 0%)
  adding: upload/12/testcase/4.in (stored 0%)
  adding: upload/12/testcase/5.in (stored 0%)
  adding: upload/12/testcase/3.in (stored 0%)
  adding: upload/12/testcase/2.out (stored 0%)
  adding: upload/12/testcase/5.out (stored 0%)
  adding: upload/12/testcase/4.out (stored 0%)
  adding: upload/12/problem.json (deflated 72%)
  adding: upload/11/ (stored 0%)
  adding: upload/11/testcase/ (stored 0%)
  adding: upload/11/testcase/2.in (stored 0%)
  adding: upload/11/testcase/1.out (stored 0%)
  adding: upload/11/testcase/3.out (stored 0%)
  adding: upload/11/testcase/1.in (stored 0%)
  adding: upload/11/testcase/4.in (stored 0%)
  adding: upload/11/testcase/5.in (stored 0%)
  adding: upload/11/testcase/3.in (stored 0%)
  adding: upload/11/testcase/2.out (stored 0%)
  adding: upload/11/testcase/5.out (stored 0%)
  adding: upload/11/testcase/4.out (stored 0%)
  adding: upload/11/problem.json (deflated 71%)
  adding: upload/9/ (stored 0%)
  adding: upload/9/testcase/ (stored 0%)
  adding: upload/9/testcase/2.in (stored 0%)
  adding: upload/9/testcase/1.out (stored 0%)
  adding: upload/9/testcase/3.out (stored 0%)
  adding: upload/9/testcase/1.in (stored 0%)
  adding: upload/9/testcase/4.in (stored 0%)
  adding: upload/9/testcase/5.in (stored 0%)
  adding: upload/9/testcase/3.in (stored 0%)
  adding: upload/9/testcase/2.out (stored 0%)
  adding: upload/9/testcase/5.out (stored 0%)
  adding: upload/9/testcase/4.out (stored 0%)
  adding: upload/9/problem.json (deflated 71%)
  adding: upload/2/ (stored 0%)
  adding: upload/2/testcase/ (stored 0%)
  adding: upload/2/testcase/2.in (stored 0%)
  adding: upload/2/testcase/1.out (stored 0%)
  adding: upload/2/testcase/3.out (stored 0%)
  adding: upload/2/testcase/1.in (stored 0%)
  adding: upload/2/testcase/4.in (stored 0%)
  adding: upload/2/testcase/5.in (stored 0%)
  adding: upload/2/testcase/3.in (stored 0%)
  adding: upload/2/testcase/2.out (stored 0%)
  adding: upload/2/testcase/5.out (stored 0%)
  adding: upload/2/testcase/4.out (stored 0%)
  adding: upload/2/problem.json (deflated 70%)
  adding: upload/3/ (stored 0%)
  adding: upload/3/testcase/ (stored 0%)
  adding: upload/3/testcase/2.in (stored 0%)
  adding: upload/3/testcase/1.out (stored 0%)
  adding: upload/3/testcase/3.out (stored 0%)
  adding: upload/3/testcase/1.in (stored 0%)
  adding: upload/3/testcase/4.in (stored 0%)
  adding: upload/3/testcase/5.in (stored 0%)
  adding: upload/3/testcase/3.in (stored 0%)
  adding: upload/3/testcase/2.out (stored 0%)
  adding: upload/3/testcase/5.out (stored 0%)
  adding: upload/3/testcase/4.out (stored 0%)
  adding: upload/3/problem.json (deflated 71%)
  adding: upload/7/ (stored 0%)
  adding: upload/7/testcase/ (stored 0%)
  adding: upload/7/testcase/2.in (stored 0%)
  adding: upload/7/testcase/1.out (stored 0%)
  adding: upload/7/testcase/3.out (stored 0%)
  adding: upload/7/testcase/1.in (stored 0%)
  adding: upload/7/testcase/4.in (stored 0%)
  adding: upload/7/testcase/5.in (stored 0%)
  adding: upload/7/testcase/3.in (stored 0%)
  adding: upload/7/testcase/2.out (stored 0%)
  adding: upload/7/testcase/5.out (stored 0%)
  adding: upload/7/testcase/4.out (stored 0%)
  adding: upload/7/problem.json (deflated 70%)
  adding: upload/8/ (stored 0%)
  adding: upload/8/testcase/ (stored 0%)
  adding: upload/8/testcase/2.in (stored 0%)
  adding: upload/8/testcase/1.out (stored 0%)
  adding: upload/8/testcase/3.out (stored 0%)
  adding: upload/8/testcase/1.in (stored 0%)
  adding: upload/8/testcase/4.in (stored 0%)
  adding: upload/8/testcase/5.in (stored 0%)
  adding: upload/8/testcase/3.in (stored 0%)
  adding: upload/8/testcase/2.out (stored 0%)
  adding: upload/8/testcase/5.out (stored 0%)
  adding: upload/8/testcase/4.out (stored 0%)
  adding: upload/8/problem.json (deflated 72%)
$ ls -lh upload.zip
-rw-rw-r-- 1 asuka asuka 37K Jun  4 19:51 upload.zip
```
