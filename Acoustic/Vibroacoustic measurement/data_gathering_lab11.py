# gathering specific data from very messy text files
# and exporting acquired data into cvs files
from pandas import DataFrame


def read_txt_file(path: str):
    file = []
    with open(path) as f:
        [file.append(l) for l in f] 
    return file


def gather_leq_data(file):
    # cutting only needed lines
    start = 34
    end = 57

    data = file[start : end]

    # and now only needed columns
    freq_idx = 1
    leq1_idx = 6
    leq2_idx = 14

    freq = []
    leq1 = []
    leq2 = []

    for i in data:
        line = i.split()
        # taking data without additional characters
        freq.append(line[freq_idx][:-2])
        try:
            leq1.append(float(line[leq1_idx][:-1]))
        except:
            leq1.append("-")
        try:
            leq2.append(float(line[leq2_idx][:-1]))
        except:
            leq2.append("-")
        
    d = {"Frequency" : freq, "Leq 1" : leq1, "Leq 2" : leq2}
    return DataFrame(data = d)
    

def gather_t20_data(file):
    # cutting only needed lines
    start = 40
    end = 63

    data = file[start : end]

    # and now only needed columns
    freq_idx = 1
    t20_idx = 8

    freq = []
    t20 = []

    for i in data:
        line = i.split()
        # taking data without additional characters
        freq.append(line[freq_idx][:-2])
        try:
            t20.append(float(line[t20_idx][:-1]))
        except:
            t20.append("-")
        
    d = {"Frequency" : freq, "T20" : t20}
    return DataFrame(data = d)


def save_data_to_file(df: DataFrame, path: str):
    df.to_csv(path, "\t", index=False)


def main():
    src_path = ""  # data filepath
    des_path = ".csv"  # path to place to save acquired data (it must end with .csv)
    t20 = True  # type of data to extract T20/LEQ (it depends on file)

    if t20:
        save_data_to_file(gather_t20_data(read_txt_file(src_path)), des_path)
    else:
        save_data_to_file(gather_leq_data(read_txt_file(src_path)), des_path)


if __name__ == '__main__':
    main()
