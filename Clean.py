def clean(input_file, output_file):
    with open(input_file, 'r') as homology_file:
        file_lines = []
        for line in homology_file:
            file_lines.append(line.split('\t'))

    file_columns = [i for i in zip(*file_lines)]

    clean_lines = []

    for row_idx, line in enumerate(file_lines):
        line_status = True
        print(row_idx)
        for col_idx, cell in enumerate(line):

            if not cell or cell == '\n':
                line_status = False

            # THIS CHECKS VEEERRRYYYY SLOOOOWWW! NEED TO OPTIMIZE! but it works
            if cell in file_columns[col_idx][0:row_idx] or cell in file_columns[col_idx][row_idx+1:]:
                line_status = False

        if line_status:
            clean_lines.append(line)

    with open(output_file, 'w') as ch:
        ch.write(''.join(['\t'.join(line) for line in clean_lines]))

clean('./output/agambiae_homology_genes.txt', './clean_homology.tsv')
