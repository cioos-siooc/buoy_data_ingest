import sys
import os

from meds_csv_fix.meds_csv_fix import fix_csv_files

if __name__ == "__main__":
    input_folder = sys.argv[1]
    output_folder = "./csv-fixed"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    fix_csv_files(input_folder, output_folder)
