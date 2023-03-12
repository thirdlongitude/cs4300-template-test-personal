import json

format_fp = open("format.txt")
data_format= format_fp.readlines()
format_fp.close()

desc_fp = open("desc.txt")
data_desc= desc_fp.readlines()
desc_fp.close()


cnt=0

print(len(data_format))
print(len(data_desc))
fp = open('sql_full.txt','w')

for i in range(len(data_format)):
    cnt += 1
    fp1 = data_format[i].rstrip('\n').replace("'", r"''")
    desc1 =  data_desc[i].rstrip('\n').replace("'", r"''")
    fp.write(f'''INSERT INTO episodes VALUE({cnt},'{fp1}','{desc1}');\n''')

fp.close()