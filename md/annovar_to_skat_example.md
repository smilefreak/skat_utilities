# Annovar annotation (mitochondrial example)

Using a VCF file of a mtDNA exmple we are going to first annotate the file, 
then convert the VCF to plink, create the SSD file for skat and read the
file into R.


Set up variables, and replace the rCRS with MT so it can be recognised by annovar.

```{bash}
    export ANNOVAR_DB=/Users/smilefreak/anna/annovar/annovar/humandb
cat pipeline_setup.txt.filter.vcf | cut -d $'\t' -f 1,2,3,4,5,6,7,8,9,10,11-  | sed "s/gi|251831106|ref|NC_012920.1|/MT/g" > pipeline_setup.txt.filter.recode.vcf

    bcftools view -s "^AT0487,AT1007,G6695,G6422"  pipeline_setup.txt.filter.recode.vcf > tmp.tmp
    mv tmp.tmp pipeline_setup.txt.filter.recode.vcf 

    convert2annovar.pl -format vcf4old pipeline_setup.txt.filter.recode.vcf --filter pass > annovar_annotate.txt
    annotate_variation.pl -buildver GRCh37_MT -dbtype ensGene annovar_annotate.txt annovar/annovar/humandb
``` 


Annotate annovar input

```{bash}
    export ANNOVAR_INPUT=/Users/smilefreak/anna/annovar_annotate.txt.exonic_variant_function

```


The next step is to convert the annotation format into groups the groups will define what the SNP should be annotated in.

But first better convert the VCF file to plink format.

```{bash}
    vcftools --vcf  pipeline_setup.txt.filter.recode.vcf  --plink  --out mtdna
    plink --file mtdna --out mtdna
```

This step in the process leaves us with two files, mtdna.map, and mtdna.ped


```{bash}
    cat annovar_annotate.txt.variant_function | grep "exonic" > exonic.txt
    anno_gene_to_skat -a exonic.txt -m mtdna.map > ssid.txt 
``` 
