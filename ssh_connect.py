import pexpect
import Multiprocess
import parse
prompt=['#','$']
def command(cmd):
  sendline(cmd)
   if 
def connect(host,user,passwd):
  ssh_con = 'ssh ' + user + '@' + host#创建一个ssh登录的命令对象
  child = pexpect.spawn(ssh_con,timeout=3)#创建一个ssh登录的子程序，
  
