import shlex
from subprocess import Popen, PIPE

def run_cmd(command_str, returncode=40000):
    """
    use shlex and subprocess to run shell commands
    you can use pipe character to connect single command together just like what you do in shell:
    ps -ef |grep rabbit | awk '{print $1}', but
    PLEASE MAKE SURE THERE IS NOT '|' IN YOUR SINGLE COMMAND
    :param command_str : string : command string
    :param returncode: int : return code when command run into errors
    """
    commands = [cmd.strip() for cmd in command_str.split('|') if cmd.strip()]
    prevous_output = None
    try:
        for command in commands:

            # Use shlex so that quoted strings won't get split
            process_as_list = shlex.split(command)
            process = Popen(
                process_as_list,
                stdout=PIPE,
                stderr=PIPE,
                stdin=PIPE,
                bufsize=-1,
                universal_newlines=True,
            )
            output, error = process.communicate(input=prevous_output)
            process_returncode = process.returncode
            if (error or process_returncode) and \
                    ('grep' not in process_as_list[0]
                     or ('grep' in process_as_list[0] and process_returncode != 1)):
                return {
                    'returncode': returncode,
                    'errmessage': error or output,
                    'data': ''
                }

            prevous_output = output

        return {
            'returncode': 0,
            'errmessage': '',
            'data': prevous_output
        }

    except OSError, os_error:
        # cmd not found error
        return {
            'data': '',
            'errmessage': 'command {0} does not exist or wrong'.format(command_str),
            'returncode': returncode
        }


if __name__ == '__main__':
    ## run scuessfuly command
    print run_cmd('/bin/ls -ls|grep zfs*')
    ## run failed command
    print run_cmd('/bin/hahah -ls|grep zfs*')
