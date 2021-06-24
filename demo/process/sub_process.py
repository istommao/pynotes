"""run subprocess"""
import subprocess

from subprocess import PIPE


def run_subprocess(cmd_str: str):
    cmd_list = cmd_str.split(' ')

    process = subprocess.run(cmd_list, stdout=PIPE, stderr=PIPE)

    if process.returncode != 0:
        result = process.stderr.decode('utf-8')
    else:
        result = process.stdout.decode('utf-8')

    return result


def main():
    cmd = "curl -I https://docs.python.org/zh-cn/3/"
    result = run_subprocess(cmd)
    print('Run cmd: {}\n'.format(cmd))
    print(result)


if __name__ == '__main__':
    main()
