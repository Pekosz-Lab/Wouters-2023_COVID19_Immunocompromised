# 2023 SARS-CoV-2 VariantCalls
Clinical SARS-CoV-2 Variant Calling scripts for [Wouters et al., 2023]() Figure X. 

## Raw Data 
* FASTQ: [Placeholder SRA Link](https://www.ncbi.nlm.nih.gov/sra)
* Sorted BAM: [Placeholder SRA Link](https://www.ncbi.nlm.nih.gov/sra)

## Variant Call Data
* [Merged_PASS_complete_calls.vcf](/data/Merged_PASS_complete_calls.vcf): Merged VCF for all isolates. 
* [merged_min11074.vcf](/data/merged_min11074.vcf): Merged VCF for all isolates **excluding** site 11074.

## Scripts 
* [vcf2pmatrix.py](/scripts/vcf2pmatrix.py): Scripts for extracting variant call matrix from VCF.
* [ratio.py](/scripts/ratio.py): Scripts for calculating REF allele ratio from call matrix.
* [variant_plot.R](/scripts/variant_plot.R): Scripts for plotting frequency. 

## Methods:

Viral genomic RNA was extracted, sequenced and subject variant calling using as previously described. Briefly, variants were called using the actic-ncov2019 medeka protocol against reference hCoV-19/Wuhan/WIV04/2019 (EPI_ISL_402124). Variants were manually instepcted against BAM files usig Integrated Genomics Viewer (v2.12.3) and Geneious Prime (2023.1.2 Build 2023-04-27). Resulting variant call files (VCFs) were indexed and merged using tabix (v1.17) and bcftools (v1.17). MergedVCFs were filtered for quality (QUAL ≥ 30) and mono-allelic variant calls. Allele frequency was calculated as the abundance of alternate allele reads over reference allele reads using `vcf2pmatrix.py` and `ratio.py`. A bi-allelic tandem repeat insertion variant at position 11,074 CT/CCT,C was removed due to visualization constraints and can be viewed in the: Merged_PASS_complete_calls.vcf. Variants were visualized using custom scripts and the pheatmap package (v1.0.12). All scripts are available at https://github.com/Pekosz-Lab/Wouters-2023_COVID19_Immunocompromised.