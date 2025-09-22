import os

from_dir = 'from'
to_dir = 'to'
output_file = os.path.join(to_dir, 'output.txt')

os.makedirs(to_dir, exist_ok=True)

with open(output_file, 'w', encoding='utf-8') as out_f:

    print(f"Processing files {len(os.listdir(from_dir))} from '{from_dir}' to '{output_file}'")

    for filename in os.listdir(from_dir):
        file_path = os.path.join(from_dir, filename)

        print(f"Processing file: {filename}")
        
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            values = []
            with open(file_path, 'r', encoding='utf-8') as in_f:
                for line in in_f:
                    if '=' in line:
                        after_eq = line.split('=', 1)[1]
                        value = after_eq.split('||', 1)[0].strip()
                        values.append(value)
            name_without_ext = os.path.splitext(filename)[0]
            out_f.write(f"{name_without_ext}=" + "/".join(values) + "\n")

print(f"Done! Output written to '{output_file}'")