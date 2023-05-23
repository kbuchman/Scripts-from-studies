# gathering specific data from very messy text files
# and exporting acquired data into cvs files
from pandas import DataFrame, concat


def read_txt_file(path: str):
    file = []
    with open(path) as f:
        [file.append(l) for l in f] 
    return file


def gather_leq_data_column(file, num):
    # cutting only needed lines
    start = 34
    end = 51

    data = file[start : end]

    # and now only needed columns
    leq1_idx = 6

    leq1 = []

    for i in data:
        line = i.split()
        # taking data without additional characters
        try:
            leq1.append(float(line[leq1_idx][:-1]))
        except:
            leq1.append("-")
        
    d = {f"{num}" : leq1}
    return DataFrame(data = d)


def save_data_to_file(df: DataFrame, path: str):
    df.to_csv(path, "\t", index=False)


def main():
    src_path = [f"D:\Studies\IV sem\Wibro\Lab 9\GR5\MOC5_{num :02d}.TXT" for num in range(1, 25)] # data filepaths
    des_path = "test.csv"  # path to place to save acquired data (it must end with .csv)
    
    columns = [gather_leq_data_column(read_txt_file(path), num + 1) for num, path in enumerate(src_path)]
    output = concat(columns, axis=1)
    save_data_to_file(output, des_path)


if __name__ == '__main__':
    main()
