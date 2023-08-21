import subprocess

if __name__ == '__main__':
result = subprocess.run(args="grep 'Ubuntu 22.04.1 LTS' /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
if result.returncode == 0:
print('True')
else:
print('False')
