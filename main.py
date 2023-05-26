import tabula
import camelot
import os
import argparse

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Input pdf file')
    # Add an argument for the input
    parser.add_argument('--input', type=str, help='Input argument')
    # Parse the command-line arguments
    args = parser.parse_args()


    file_path = args.input


    dfs = tabula.read_pdf(file_path, pages='all')

    outputDir = 'output'
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    for i, table in enumerate(dfs):
        table.to_csv(outputDir + '/output_' + str(i + 1) + '.csv')

    print("Total tables extracted:", len(dfs))

if __name__ == '__main__':
    main()