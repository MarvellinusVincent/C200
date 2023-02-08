# Midterm Programming Exam

- Username: mvincen
- Commit hash used for grading: 633bf7aa75f4f9e76455d52d58776a0712152daa

- Graded by: Ankush Pathak

Rubric:

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 30         |
| Code Review   | 30         |



## Total Score: 57.2/60
- Please double-check that your Canvas score reflects what is shown here. 
- The programming section of the midterm has 60% of the total grade. The remaining 40% is for the quiz that you took on Canvas. 

## Code Tests (29.17/30 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `f`: 10.0/10
    - TA Comments: All good!


- Problem 2:
    - `gravity`: 10.0/10
    - TA Comments: All good!


- Problem 3:
    - `tip_amt`: 9.2/10
    - TA Comments: You forgot to round the answer to two decimal places.



## Code Review & style (28/30 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

- Problem 1:
    - `f`: 10/10
    - TA Comments: Good job! Try avoiding built-in functions like `append` unless we explicitly tell you it's okay.


- Problem 2:
    - `gravity`: 10/10
    - TA Comments: Good job!


- Problem 3:
    - `tip_amt`: 8/10
    - TA Comments: You missed an important instruction from the problem.



## Unittest Results
```
ERROR: ============================================================================
ERROR: Failed test case: test_tipamt_1_hidden
ERROR: Test case for function: tip_amt
ERROR: Input: ((8.125, 'great'),) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: 10.15625
ERROR: Expected output: 10.16
ERROR: 10.16 != 10.15625
ERROR: ----------------------------------------------------------------------------
ERROR: 10.16 != 10.15625
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/midterm/mvincen/midterm_tests.py", line 50, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: 10.16 != 10.15625
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_tipamt_1_hidden
ERROR: Test case for function: tip_amt
ERROR: Input: ((8.125, 'bad'),) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: 9.34375
ERROR: Expected output: 9.34
ERROR: 9.34 != 9.34375
ERROR: ----------------------------------------------------------------------------
ERROR: 9.34 != 9.34375
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/midterm/mvincen/midterm_tests.py", line 50, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: 9.34 != 9.34375
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_tipamt_1_hidden
ERROR: Test case for function: tip_amt
ERROR: Input: ((8.121, 'great'),) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: 10.151250000000001
ERROR: Expected output: 10.15
ERROR: 10.15 != 10.151250000000001
ERROR: ----------------------------------------------------------------------------
ERROR: 10.15 != 10.151250000000001
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/midterm/mvincen/midterm_tests.py", line 50, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: 10.15 != 10.151250000000001
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_tipamt_1_hidden
ERROR: Test case for function: tip_amt
ERROR: Input: ((8.121, 'good'),) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: 9.7452
ERROR: Expected output: 9.75
ERROR: 9.75 != 9.7452
ERROR: ----------------------------------------------------------------------------
ERROR: 9.75 != 9.7452
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/midterm/mvincen/midterm_tests.py", line 50, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: 9.75 != 9.7452
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_tipamt_1_hidden
ERROR: Test case for function: tip_amt
ERROR: Input: ((8.121, 'bad'),) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: 9.33915
ERROR: Expected output: 9.34
ERROR: 9.34 != 9.33915
ERROR: ----------------------------------------------------------------------------
ERROR: 9.34 != 9.33915
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/midterm/mvincen/midterm_tests.py", line 50, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: 9.34 != 9.33915
ERROR: ============================================================================
```
```
