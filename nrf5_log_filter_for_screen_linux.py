def read_and_clean_Lines():
    cleanFileList = []
    with open('screen_acm0.log', 'r') as f:
        for _ in range(0, 491720):
            line = f.readline()
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

                cleanFileList.append(line)

    return cleanFileList


def write_to_file(cleanFileList):
    with open('screen_acm1.log', 'w') as f:
        for i in range(0, len(cleanFileList)):
            f.write(str(cleanFileList[i]) + '\n')


cleanFileList = read_and_clean_Lines()
write_to_file(cleanFileList)
