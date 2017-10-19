# python_run_command

python_run_command is a tools for python run complicated Unix command

1: run_cmd('/bin/ls -ls|grep zfs*') success

return :

{'errmessage': '', 'returncode': 0, 'data': '   4 drwxrwxr-x 13 8331 8331    4096 Jun 26 05:12 zfs-0.6.5.2\n2456 -rw-r--r--  1 root root 2512396 May 21 05:19 zfs-0.6.5.2.tar.gz\n'}




2: run_cmd('/bin/hahah -ls|grep zfs*') failed

return:

{'errmessage': 'command /bin/hahah -ls|grep zfs* does not exist or wrong', 'returncode': 40000, 'data': ''}

