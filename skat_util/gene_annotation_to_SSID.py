#
#
# Takes two arguments, a map file, and a annovar input.
#


import argparse


snps = {}

def process_snps(map_file):
    with open(map_file) as map_f:
        for line in map_f:
            line = line.split("\t")
            snp_name = line[1]
            snps[snp_name] = []


def process_annovar(annovar):
    with open(annovar) as anno_f:
        for line in anno_f:
            line = line.split('\t')
            gene = line[1]
            chrom = line[2]
            pos = line[3]
            snp_name = chrom + ":" + pos
            try:
                snps[snp_name].append(gene)
            except KeyError:
                snps[snp_name] = [gene]

def output_ssid():
    for key,value in snps.items():
        for gene in value:
            print gene, key

def main():
    parser = argparse.ArgumentParser(description="Takes a PLINK map file, which contains the SNPS, plus a annovar output file from a genic annotation")
    parser.add_argument("-a","--annovar",dest="annovar",help="Annovar output file containing SNP locations")
    parser.add_argument("-m","--map",dest="map_file",help="PLINK Map file")
    args = parser.parse_args()
    assert args.map_file is not None, "-m argument needs to be set" 
    assert args.annovar is not None, "-a argument needs to be set"
    process_snps(args.map_file)
    process_annovar(args.annovar)
    output_ssid()

if __name__=="__main__":
    main()
