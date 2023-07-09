# 2023 SARS-CoV-2 VariantCalls
Clinical SARS-CoV-2 Variant Calling scripts for [Wouters et al., 2023]() Figure X. 

### Raw Data 
* FASTQ: [Placeholder SRA Link](https://www.ncbi.nlm.nih.gov/sra)
* Sorted BAM: [Placeholder SRA Link](https://www.ncbi.nlm.nih.gov/sra)

### Variant Call Data
* [Merged_PASS_complete_calls.vcf](/data/Merged_PASS_complete_calls.vcf): Merged VCF for all isolates. 
* [merged_min11074.vcf](/data/merged_min11074.vcf): Merged VCF for all isolates **excluding** site 11074.

### Scripts 
* [vcf2pmatrix.py](/scripts/vcf2pmatrix.py): Scripts for extracting variant call matrix from VCF.
* [ratio.py](/scripts/ratio.py): Scripts for calculating REF allele ratio from call matrix.
* [variant_plot.R](/scripts/variant_plot.R): Scripts for plotting frequency. 

### Methods:

RNA was extracting using -Filler- and sequenced using -FILLER- chemistry. Raw FASTQ files were assembled to the hCoV-19/Wuhan/WIV04/2019 (GISAID EPI_ISL_402124) using -FILLER-. ** Need base calling pipeline from fast5 to fastQ to BAM** BAM files were imported into Geneious Prime (2023.1.2 Build 2023-04-27) and variants were called using Freebayes (v1.1.0). Resulting variant call files (VCFs) were then indexed and merged using tabix (v1.17) and bcftools (v1.17). VCFs were filtered for quality (QUAL ≥ 30), read depth (DP ≥ 10) and mono-allelic variant calls. Variants were formatted and visualized using custom python scripts and pheatmap package (R v1.0.12) available at https://github.com/Pekosz-Lab/Wouters-2023_COVID19_Immunocompromised.

### Results:

VCF filtering across the 6 patient genomes yielded a total of 94 total polymorphic sites (Figure Xa.) A bi-allelic tandem repeat insertion variant at position 11,074 CT/CCT,C was removed due to visualization constraints and can be viewed here: [Merged_PASS_complete_calls.vcf](/data/Merged_PASS_complete_calls.vcf). 

TODO:

1. Camille Decide on what supplementary files to include in paper vs github (VCF tables).
2. Request remaining FASTQ file from rerun sample - Amary
3. Upload FASTQ files to SRA
4. Upload BAM Files to SRA
5. Convert Github repo to public.