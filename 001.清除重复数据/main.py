import os
from collections import OrderedDict
os.chdir('./001.清除重复数据')

def remove_duplicates(folder_path,new_folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):   #打开以.txt结尾的文件

            file_path = os.path.join(folder_path,filename)
            new_file_path = os.path.join(new_folder_path,filename)

            with open(file_path,'r') as f:
                lines = f.readlines()   #按行读文件

            unique_lines = OrderedDict()    #使用有序字典保持原有顺序和去重

            for line in lines:
                unique_lines[line.strip()] = None   #使用字典的链来去重，值可以为任意非空值

            #将去重后的内容写到新文件夹中
            with open(new_file_path,'w') as f:
                f.writelines("\n".join(unique_lines.keys())+"\n")   #添加换行符
            print(f"去除重复行后的文件'{file_path}'已更新。")
            


folder_path = './test/origin/'
new_folder_path = './test/clear/'
remove_duplicates(folder_path,new_folder_path)
