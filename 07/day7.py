tot_folders = {}
folder = []
total = 0
list_folder = False
def folder_name(fdr):
    return '/' + '/'.join(folder)
    
with open('input.txt') as input:
    for line in input:
        tokens = line.strip().split()
        if tokens[0]=='$':
            if list_folder:
                tot_folders[folder_name(folder)] = total
                list_folder = False
                total = 0
            if tokens[1]=='cd':
                if tokens[2]=='/':
                    folder = []
                elif tokens[2]=='..':
                    child_total = tot_folders[folder_name(folder)]
                    folder.pop()
                    tot_folders[folder_name(folder)] += child_total
                else:
                    folder.append(tokens[2])
                #print(folder_name(folder))
            elif tokens[1]=='ls':
                list_folder = True
        else:
            if list_folder and tokens[0].isnumeric():
                total += int(tokens[0])
if list_folder:
    tot_folders[folder_name(folder)] = total
while folder:
    child_total = tot_folders[folder_name(folder)]
    folder.pop()
    tot_folders[folder_name(folder)] += child_total
under_100k = [tot_folders[x] for x in tot_folders.keys() if tot_folders[x] <= 100000]
print(sum(under_100k))