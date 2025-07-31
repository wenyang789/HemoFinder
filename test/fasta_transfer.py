import pandas as pd

# test data prcessing ----
# Read CSV file
csv_file = '/Users/wendy_1/Github/HemoFinder/test/test.csv'  
df = pd.read_csv(csv_file)

# Write CSV file into FASTA file
fasta_file = 'test.fasta'
with open(fasta_file, 'w') as f:
    for index, row in df.iterrows():
        sequence = row['Sequence']
        label = row['Label']
        f.write(f'>{index}_{label}\n')	# Use raw index and label as title
        f.write(f'{sequence}\n')

# train data processing ----
# Read CSV file
csv_file = '/Users/wendy_1/Github/HemoFinder/test/train.csv'  
df = pd.read_csv(csv_file)

# Write CSV file into FASTA file
fasta_file = 'train.fasta'
with open(fasta_file, 'w') as f:
    for index, row in df.iterrows():
        sequence = row['Sequence']
        label = row['Label']
        f.write(f'>{index}_{label}\n')
        f.write(f'{sequence}\n')
