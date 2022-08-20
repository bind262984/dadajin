import  subprocess
import sys
from randpass  import gen_pass

def adduser(username, password, fname):
    data = '''user information:
    %s: %s
    '''

    subprocess.call('useradd %s' % username, shell=True)
    subprocess.call(
           'echo %s | passwd --stdin %s' % (password, username),
           shell=True
       )
    with open(fname, 'a') as fobj:
           fobj.write(data % (username, password))

if __name__ == '__main__':
    username = sys.argv[0]
    password = gen_pass()
    adduser(username, password,r"D:\user.txt")