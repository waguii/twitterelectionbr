import os


def split(filename, chunk_size=120000):
    def write_chunk(part, lines):
        with open('/home/wagui/code/waguii/twitterelectionbr/raw_data/data/totals/split/data_part_'+ str(part) +'.csv', 'w') as f_out:
            f_out.write(header)
            f_out.writelines(lines)
    with open(filename, "r") as f:
        count = 0
        header = f.readline()
        lines = []
        for line in f:
            count += 1
            lines.append(line)
            if count % chunk_size == 0:
                write_chunk(count // chunk_size, lines)
                lines = []
        # write remainder
        if len(lines) > 0:
            write_chunk((count // chunk_size) + 1, lines)

if __name__ == '__main__':
    split('/home/wagui/code/waguii/twitterelectionbr/raw_data/data/totals/query_to_lula.csv')
