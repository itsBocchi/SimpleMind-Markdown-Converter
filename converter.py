import sys, os
import tkinter
from tkinter import filedialog

try:
    file_path = sys.argv[1]
    print(file_path)
except IndexError:
    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
    file_path = filedialog.askopenfilename()
    print(file_path)

# read file as utf-8
file = open(file_path, 'r', encoding='utf-8')
lines = file.readlines()
new_lines = []
nota = ''
tab_count = 0


if lines[0].startswith('\ufeff'):
    lines[0] = lines[0][1:]
new_lines.append('### ' + lines[0].strip() + '\n')
is_nota = False

for i in range(1, len(lines)):
    if lines[i].strip() != '':
        tabs = ''
        if (lines[i][:8] == '\t\t\t\t\t\t\t\t'):
            tabs = '                '
        elif (lines[i][:7] == '\t\t\t\t\t\t\t'):
            tabs = '              '
        elif (lines[i][:6] == '\t\t\t\t\t\t'):
            tabs = '            '
        elif (lines[i][:5] == '\t\t\t\t\t'):
            tabs = '          '
        elif (lines[i][:4] == '\t\t\t\t'):
            tabs = '        '
        elif(lines[i][:3] == '\t\t\t'):
            tabs = '      '
        elif(lines[i][:2] == '\t\t'):
            tabs = '    '
        elif(lines[i][:1] == '\t'):
            tabs = '  '

        if (is_nota and lines[i].strip().startswith(']')):
            is_nota = False
            new_lines.append(tabs+ ' \| Nota: ' + nota + '\n')
            nota = ''
            continue
        elif (is_nota):
            nota = nota+lines[i].strip()+'. '
            continue
        elif (lines[i].strip().startswith('[') and not is_nota):
            is_nota = True
            continue
        else:
            new_lines.append(tabs + '- ' + lines[i].strip() + '\n')



try:
    # get file name from file_path
    file_name = file_path.split('/')[-1].split('.')[0]

except IndexError:
    file_name = file_path.split('\\')[-1].split('.')[0]


try:
    # make a folder with the same name as the file
    os.makedirs(file_name)
except FileExistsError:
    print('Folder already exists')
    pass

write_file = open('.\\'+ file_name + '\\' + file_name + '.md', 'w', encoding='utf-8')
write_file.writelines(new_lines)
write_file.close()
file.close()