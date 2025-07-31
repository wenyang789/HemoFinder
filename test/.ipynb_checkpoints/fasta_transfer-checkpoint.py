import pandas as pd

# 读取CSV文件
csv_file = '/Users/wendy/Desktop/HemoFinder_test/test.csv'  
df = pd.read_csv(csv_file)

# 打开FASTA文件用于写入
fasta_file = 'test.fasta'
with open(fasta_file, 'w') as f:
    # 遍历每一行
    for index, row in df.iterrows():
        sequence = row['Sequence']
        label = row['Label']
        # 写入FASTA格式
        f.write(f'>{index}_{label}\n')  # 使用行号和Label作为FASTA标题
        f.write(f'{sequence}\n')  # 写入序列

# 读取CSV文件
csv_file = '/Users/wendy/Desktop/HemoFinder_test/train.csv'  
df = pd.read_csv(csv_file)

# 打开FASTA文件用于写入
fasta_file = 'train.fasta'
with open(fasta_file, 'w') as f:
    # 遍历每一行
    for index, row in df.iterrows():
        sequence = row['Sequence']
        label = row['Label']
        # 写入FASTA格式
        f.write(f'>{index}_{label}\n')  # 使用行号和Label作为FASTA标题
        f.write(f'{sequence}\n')  # 写入序列