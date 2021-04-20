import sys


def finding_response(file_name):
    with open(file_name, 'r') as f:
        list_of_mid_data = []
        for line in f:
            allow = False
            if 'COAP: /config GET response received from' in line:
                allow = True
            elif '/all_status response received from' in line:
                allow = True

            if allow:
                split_line = line.split(',')
                mid = split_line[1]
                mid_data = mid.split(':')[1]
                item = (line, int(mid_data))
                list_of_mid_data.append(item)

    return list_of_mid_data


def finding_inequality(s):
    mistake = 0
    for i in range(0, len(s)-1):
        if s[i][1] > s[i+1][1]:
            mistake += 1
            print(str(s[i][0]) + str(s[i+1][0]))

    return mistake


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Error: input file missed!')
        exit()

    file_name = sys.argv[1]
    list_of_responses = finding_response(file_name)
    errors = finding_inequality(list_of_responses)
    error_rate = errors*100//len(list_of_responses)
    print('total: ' + str(len(list_of_responses)) +
          ' | errors: ' + str(errors) +
          ' | error rate: ' + str(error_rate) + '%')
