def merge_files_with_headers(file_names, output_file_name):
    header_separator = "=== Содержимое {} ===\n"
    with open(output_file_name, 'w', encoding='utf-8') as outfile:
        for filename in file_names:
            outfile.write(header_separator.format(filename))
            with open(filename, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write('\n\n')

file_names = ['file1.txt', 'file2.txt', 'file3.txt']
output_file_name = 'resource/combined.txt'

merge_files_with_headers(file_names, output_file_name)