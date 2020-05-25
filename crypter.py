import os, sys

#crypt function
def read_and_crypt(path, key):
	read = [];
	encrypt = [];
	with open(path, 'r+') as file:
		for i in file:
			read += i;

	for i in read:
		encrypt += chr(ord(i) ^ int(key));

	path2 = path + '.crypt';
	
	with open(path2, 'a+') as file:
		for i in encrypt:
			file.write(i);