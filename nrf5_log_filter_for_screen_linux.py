import sys


def read_and_clean_lines(file_name):
    clean_file_list = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line[:-1]
            if line:
                line = line.replace('\x1b[1;32musb_cli:~$ \x1b[1;37m\x1b[11D\x1b[J\x1b[0m', '')
                line = line.replace('\x1b[1;32musb_cli:~$ \x1b[1;37m\x1b[11D\x1b[J\x1b[1;31m', '')
                line = line.replace('\x1b[1;32musb_cli:~$ \x1b[1;37m\x1b[11D\x1b[J\x1b[1;33m', '')
                line = line.replace('\x1b[11D\x1b[J\x1b[1;31m', '')
                line = line.replace('\x1b[1;32musb_cli:~$ \x1b[1;37mstat\x1b[15D\x1b[J', '')
                line = line.replace('\x1b[1;32musb_cli:~$ \x1b[1;37mstatus\x1b[17D\x1b[J\x1b[0m', '')
                line = line.replace('\x1b[1;32musb_cli:~$ \x1b[1;37mstatus\x1b[17D\x1b[J\x1b[1;33m', '')
                line = line.replace('\x1b[1;32musb_cli:~$ \x1b[1;37mstatus', '')
                line = line.replace('\x1b[0m', '')

                clean_file_list.append(line)

    return clean_file_list


def write_to_file(s, file_name):
    with open(file_name, 'w') as f:
        for i in range(0, len(s)):
            f.write(str(s[i]) + '\n')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('nrf5_log_filter_for_screen_linux.py [input_file] [output_file]\n' +
              'Error: arguments missed!')
        exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    filtered_list = read_and_clean_lines(input_file)
    write_to_file(filtered_list, output_file)
