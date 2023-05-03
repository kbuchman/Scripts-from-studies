# gathering specific data from very messy text files
from pandas import DataFrame


PATH = "filepath"


def read_txt_file(path):
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


save_data_to_file(gather_t20_data(read_txt_file(PATH)), f"test.csv")