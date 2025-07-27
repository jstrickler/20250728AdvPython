from configparser import ConfigParser
import paramiko
# bc is an interactive calculator that comes with Unix-like systems (Linux, Mac, etc.)

config = ConfigParser()
config.read('sdfauth.ini')

with paramiko.SSHClient() as ssh:  # create paramiko SSH client
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # auto-add remote host

    ssh.connect(
        config['auth']['hostname'],
        username=config['auth']['username'], 
        password=config['auth']['password'],
    )  # log into to remote host

    stdin, stdout, stderr = ssh.exec_command('bc')  # execute command; returns file-like objects representing stdio

    stdin.write("17 + 25\n")  # write to command's stdin
    result = stdout.readline()  # read output of command
    print("Result is:", result)

    stdin.write("scale = 3\n")  # set scale (# decimal points) to 3 (bc-specific command)
    stdin.write("738.3/191.9\n")
    result = stdout.readline()
    print("Result is:", result)
    stdin.write("quit\n")  # create paramiko SSH client

    # create remote file
    ssh.exec_command('touch wombats.txt')
    stdin, stdout, stderr = ssh.exec_command('ls -l')
    print(stdout.read().decode())

    # remove remote file interactively
    stdin, stdout, stderr = ssh.exec_command('rm -i wombats.txt')
    stdin.write('y\n')

    # show that remote file is no longer there
    stdin, stdout, stderr = ssh.exec_command('ls -l')
    print(stdout.read().decode())

    stdin = None   # needed for cleanup



