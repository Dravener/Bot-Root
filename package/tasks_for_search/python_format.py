import re


def python_format(text):
    bit_content = ''
    text_la = text.split('\n')  # split text into lines
    index = 100
    sps = 0
    function_name = ''
    if len(text_la) > 1:  # array with text lines range
        for line in range(len(text_la)):  # looping through that array
            key_name = re.search(r'def\s*.*\(.*\)\:', text_la[line])  # find string in the line
            nam = re.search(r'(?<=def\s)(.*)(?=\(.*\))', text_la[line])  # find string in the line
            if bit_content == '' and key_name is not None:
                sp = text_la[line].split('def')  # split line
                dd = len(sp[0])
                aa = text_la[line][dd:]
                index = line
                sps = dd
                if function_name is not None:
                    function_name = nam.group(0)
                if aa in bit_content:
                    pass
                else:
                    bit_content += str(aa) + '\n'
            else:
                bit_content += ''
            if line > index:
                aaa = text_la[line][sps:]
                if aaa.startswith('    '):
                    if aaa in bit_content:
                        pass
                    else:
                        bit_content += str(aaa) + '\n'
                else:
                    bit_content += ''
            else:
                bit_content += ''
    else:
        bit_content += ''
    checking = bit_content.split('\n')
    if len(checking) > 1 and checking[1] != '':
        items = {"text": bit_content, "nam": function_name}
        return items
    else:
        items = {"text": '', "nam": ''}
        return items

