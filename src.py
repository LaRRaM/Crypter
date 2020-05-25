import os, sys, time
import crypter as crypt

def path(dir, key):
	if os.path.exists(dir) and not os.path.isfile(dir):
		for name in os.listdir(dir):
			path = os.path.join(dir, name);
			if os.path.isfile(path):
				crypt.read_and_crypt(path, key);
				os.remove(path);
				print('[\033[32m ENCRYPTED \033[0m] - ', path);
			else:
				path(path);
	elif os.path.isfile(dir):
		crypt.read_and_crypt(dir, key);
		os.remove(dir);
	else:
		print('\033[31m[ ERR ] - Path not exist!\033[31m');

def main():
	try:
		_key_ = int(input('[ ASK ] - Key for encrypt >>> '));
	except:
		print('\033[31m[ ERR ] - Only integer keys!\033[31m');
	_pwd_ = input('[ ASK ] - Path to crypt >>> ');
	_ask_ = input('[ ASK ] - Sure what you want to do it? \n [ Y/N ] >>> ');
	if _ask_ == 'Y' or _ask_ == 'y' or _ask_ == 'Yes' or _ask_ == 'yes':
		path(_pwd_, _key_);
	else:
		print('Ok, bye!');


if __name__ == '__main__':
	main();

#SlkfSdkBjbm :: 5
