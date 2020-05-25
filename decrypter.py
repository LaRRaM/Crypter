import os, sys

def read_and_decrypt(path, key):
	read = [];
	decrypt = [];
	with open(path, 'r+') as file:
		for i in file:
			read += i;

	for i in read:
		try:
			decrypt += chr(ord(i) ^ ord(key));
		except TypeError:
			decrypt += chr(ord(i) ^ int(key));

	path2 = path[0: -6]

	with open(path2, 'a+') as file:
		for i in decrypt:
			file.write(i);
def main():
	key = input('[ KEY ] >>> ');
	path = input('[ FILE ] >>> ');
	read_and_decrypt(path, key);

if __name__ == '__main__':
	main();
