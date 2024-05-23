# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"442D000","system":"readv2"},{"code":"442D.00","system":"readv2"},{"code":"442D100","system":"readv2"},{"code":"L4031AN","system":"readv2"},{"code":"L4031AA","system":"readv2"},{"code":"L4031","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('thyroid-function-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["thyroid-function-uptake---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["thyroid-function-uptake---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["thyroid-function-uptake---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
