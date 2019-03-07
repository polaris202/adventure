import  os,sys,shutil,re


# result = re.match(pattern, string)

path1 = "/home/kuro/Daten/tmp/mydir_1/"
path2 = "/home/kuro/Daten/tmp/mydir_2/"
path3 = "/home/kuro/Daten/tmp/mydir_3/"
path4 = "/home/kuro/Daten/tmp/mydir_4/"


dir1 = os.listdir(path1)

result = re.search('.*bak.*', str(dir1))

print(dir1)
print(result)