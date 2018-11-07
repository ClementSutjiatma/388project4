
#!/usr/bin/python
import subprocess
import os
import base64
import sys
import random
import string
from random import randint

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
test =  "1234567"
special =  ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')','{', '\'', '~','`','"', '""']
possible_values = []
i = 0
sample = '''{"header": "value"}'''
samplewithnum = '''{"header": value}'''
failureTestCases = []
for value in special:
	failureTestCases.append(sample.replace("header", test.replace("3", value)))
string_length = 200

rand_str = lambda n: ''.join([random.choice(string.lowercase) for i in xrange(n)])

failureTestCases.append(sample.replace("header", rand_str(100000)))
failureTestCases.append(sample.replace("header", rand_str(10000)))
failureTestCases.append(sample.replace("header", rand_str(1000)))
failureTestCases.append(sample.replace("header", rand_str(100)))
failureTestCases.append(samplewithnum.replace("value",str(random.uniform(1E-100, 1E-101))))
failureTestCases.append(samplewithnum.replace("value",str(random.uniform(1E-1000, 1E-1001))))
failureTestCases.append(samplewithnum.replace("value",str(random.uniform(1E-10000, 1E-10001))))


failureTestCases.append(samplewithnum.replace("value",str(randint (1E100, 1E101))))
hardcoded = [
   '''{"same": "first", "same": "second"}''',
   '''{"weird_int":123_456, "second_layer": { "something": "value"}}''',
   '''{""": "val"}''',
   '''{: 123}''',
   '''{"hello":{"value"}''',
   '''{{{}}}''',
   '''0{"lol": "portugal"}''',
   '''{"\n": "\n"}''',
   '''{\x86:"stop"}'''
   '''{"l": "lol", "k"}''',
   '''{[1,2,a,b]: "something"}''',
   '''{"true":"false"}''',
   '''{"true":"falsetrue"}''',
   '''{"boolean":"false true false"}''',
   '''{"something":0}''',
   '''{"both_true_and_false":01}''',
   '''{"first": {"second": {"third": {"fourth": "lol"}}}}''',
   '''{"first": {}, {"second" {}}}'''
]

for item in hardcoded:
	failureTestCases.append(item)

for testcase in failureTestCases:
    child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    _, stdErrOut = child.communicate(input = testcase)
    #if child.returncode != 0 or stdErrOut == "" :
        #print "BROKEN FAILURE TEST CASE (%d): %s" % (child.returncode, testcase)
        #print "|%s|" % stdErrOut
    if child.returncode == -11:
	#print "SEGFAULTED YAY!"
	print base64.b64encode(testcase)

 
