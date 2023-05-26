import tabula
import camelot
import os
import argparse

# from PyPDF2 import PdfReader

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Input pdf file')
    # Add an argument for the input
    parser.add_argument('--input', type=str, help='Input argument')
    # Parse the command-line arguments
    args = parser.parse_args()

    # file_path = "/Users/zacdean/projects/Upzone/Housing Elements/San Diego/cities/San Diego/he_appd_sitesinventoryreport_final.pdf"
    # file_path = "/Users/zacdean/projects/Upzone/Housing Elements/San Diego/cities/San Diego/he_adequatesites_final_13feb13.pdf"
    # file_path = "/Users/zacdean/projects/Upzone/Housing Elements/San Diego/cities/Carlsbad/Adopted Housing Element.pdf"
    file_path = args.input
    # tables = camelot.read_pdf(file_path, pages='all')

    dfs = tabula.read_pdf(file_path, pages='all')
    #  guess=True, multiple_tables=True
    # reader = PdfReader(file_path)
    # number_of_pages = len(reader.pages)
    # page = reader.pages[0]
    # text = page.extract_text()

    # tables = reader.tables

    # for table in tables:
    #     print(table.data)
    outputDir = 'output'
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    for i, table in enumerate(dfs):
        table.to_csv(outputDir + '/output_' + str(i + 1) + '.csv')
    # dfs[0].to_csv(outputDir + '/output.csv')

    # print(number_of_pages)
    print("Total tables extracted:", len(dfs))

if __name__ == '__main__':
    main()