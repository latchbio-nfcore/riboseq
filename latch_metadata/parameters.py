
from dataclasses import dataclass
import typing
import typing_extensions

from flytekit.core.annotation import FlyteAnnotation

from latch.types.metadata import NextflowParameter
from latch.types.file import LatchFile
from latch.types.directory import LatchDir, LatchOutputDir

# Import these into your `__init__.py` file:
#
# from .parameters import generated_parameters

generated_parameters = {
    'input': NextflowParameter(
        type=LatchFile,
        default=None,
        section_title='Input/output options',
        description='Path to comma-separated file containing information about the samples in the experiment.',
    ),
    'contrasts': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='A CSV file describing sample contrasts',
    ),
    'outdir': NextflowParameter(
        type=typing_extensions.Annotated[LatchDir, FlyteAnnotation({'output': True})],
        default=None,
        section_title=None,
        description='The output directory where the results will be saved. You have to use absolute paths to storage on Cloud infrastructure.',
    ),
    'email': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Email address for completion summary.',
    ),
    'multiqc_title': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='MultiQC report title. Printed as page header, used for filename if not otherwise specified.',
    ),
    'genome': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Reference genome options',
        description='Name of iGenomes reference.',
    ),
    'fasta': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to FASTA genome file.',
    ),
    'gtf': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to GTF annotation file.',
    ),
    'gff': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to GFF3 annotation file.',
    ),
    'transcript_fasta': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Path to FASTA transcriptome file.',
    ),
    'additional_fasta': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='FASTA file to concatenate to genome FASTA file e.g. containing spike-in sequences.',
    ),
    'star_index': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Path to directory or tar.gz archive for pre-built STAR index.',
    ),
    'salmon_index': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Path to directory or tar.gz archive for pre-built Salmon index.',
    ),
    'gencode': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Specify if your GTF annotation is in GENCODE format.',
    ),
    'gtf_extra_attributes': NextflowParameter(
        type=typing.Optional[str],
        default='gene_name',
        section_title=None,
        description='By default, the pipeline uses the `gene_name` field to obtain additional gene identifiers from the input GTF file when running Salmon.',
    ),
    'gtf_group_features': NextflowParameter(
        type=typing.Optional[str],
        default='gene_id',
        section_title=None,
        description='Define the attribute type used to group features in the GTF file when running Salmon.',
    ),
    'trimmer': NextflowParameter(
        type=typing.Optional[str],
        default='trimgalore',
        section_title='Read trimming options',
        description="Specifies the trimming tool to use - available options are 'trimgalore' and 'fastp'.",
    ),
    'extra_trimgalore_args': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Extra arguments to pass to Trim Galore! command in addition to defaults defined by the pipeline.',
    ),
    'extra_fastp_args': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Extra arguments to pass to fastp command in addition to defaults defined by the pipeline.',
    ),
    'min_trimmed_reads': NextflowParameter(
        type=typing.Optional[int],
        default=10000,
        section_title=None,
        description='Minimum number of trimmed reads below which samples are removed from further processing. Some downstream steps in the pipeline will fail if this threshold is too low.',
    ),
    'bbsplit_fasta_list': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title='Read filtering options',
        description='Path to comma-separated file containing a list of reference genomes to filter reads against with BBSplit. You have to also explicitly set `--skip_bbsplit false` if you want to use BBSplit.',
    ),
    'bbsplit_index': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Path to directory or tar.gz archive for pre-built BBSplit index.',
    ),
    'sortmerna_index': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Path to directory or tar.gz archive for pre-built sortmerna index.',
    ),
    'remove_ribo_rna': NextflowParameter(
        type=typing.Optional[bool],
        default=True,
        section_title=None,
        description='Enable the removal of reads derived from ribosomal RNA using SortMeRNA.',
    ),
    'ribo_database_manifest': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Text file containing paths to fasta files (one per line) that will be used to create the database for SortMeRNA.',
    ),
    'with_umi': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title='UMI options',
        description='Enable UMI-based read deduplication.',
    ),
    'umitools_extract_method': NextflowParameter(
        type=typing.Optional[str],
        default='string',
        section_title=None,
        description="UMI pattern to use. Can be either 'string' (default) or 'regex'.",
    ),
    'umitools_bc_pattern': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description="The UMI barcode pattern to use e.g. 'NNNNNN' indicates that the first 6 nucleotides of the read are from the UMI.",
    ),
    'umitools_bc_pattern2': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='The UMI barcode pattern to use if the UMI is located in read 2.',
    ),
    'umi_discard_read': NextflowParameter(
        type=typing.Optional[int],
        default=None,
        section_title=None,
        description='After UMI barcode extraction discard either R1 or R2 by setting this parameter to 1 or 2, respectively.',
    ),
    'umitools_umi_separator': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='The character that separates the UMI in the read name. Most likely a colon if you skipped the extraction with UMI-tools and used other software.',
    ),
    'umitools_grouping_method': NextflowParameter(
        type=typing.Optional[str],
        default='directional',
        section_title=None,
        description='Method to use to determine read groups by subsuming those with similar UMIs. All methods start by identifying the reads with the same mapping position, but treat similar yet nonidentical UMIs differently.',
    ),
    'umitools_dedup_stats': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Generate output stats when running "umi_tools dedup".',
    ),
    'aligner': NextflowParameter(
        type=typing.Optional[str],
        default='star',
        section_title='Alignment options',
        description="Specifies the alignment algorithm to use - available options are currently 'star'.",
    ),
    'pseudo_aligner_kmer_size': NextflowParameter(
        type=typing.Optional[int],
        default=31,
        section_title=None,
        description='Kmer length passed to indexing step of pseudoaligners',
    ),
    'bam_csi_index': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Create a CSI index for BAM files instead of the traditional BAI index. This will be required for genomes with larger chromosome sizes.',
    ),
    'star_ignore_sjdbgtf': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='When using pre-built STAR indices do not re-extract and use splice junctions from the GTF file.',
    ),
    'salmon_quant_libtype': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description=' Override Salmon library type inferred based on strandedness defined in meta object.',
    ),
    'min_mapped_reads': NextflowParameter(
        type=typing.Optional[float],
        default=5.0,
        section_title=None,
        description='Minimum percentage of uniquely mapped reads below which samples are removed from further processing.',
    ),
    'seq_center': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Sequencing center information to be added to read group of BAM files.',
    ),
    'extra_star_align_args': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Extra arguments to pass to STAR alignment command in addition to defaults defined by the pipeline. Only available for the STAR-Salmon route.',
    ),
    'extra_salmon_quant_args': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Extra arguments to pass to Salmon quant command in addition to defaults defined by the pipeline.',
    ),
    'extra_ribotish_quality_args': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Riboseq-specific options',
        description='Extra arguments to pass to the ribotish quality command in addition to defaults defined by the pipeline.',
    ),
    'extra_ribotish_predict_args': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Extra arguments to pass to the ribotish predict command in addition to defaults defined by the pipeline.',
    ),
    'extra_ribotricer_prepareorfs_args': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Extra arguments to pass to the ribotricer prepare-orfs command in addition to defaults defined by the pipeline.',
    ),
    'extra_ribotricer_detectorfs_args': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Extra arguments to pass to the ribotricer detect-orfs command in addition to defaults defined by the pipeline.',
    ),
    'extra_anota2seq_run_args': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Extra arguments to pass to anota2seq in addition to defaults defined by the pipeline.',
    ),
    'save_merged_fastq': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title='Optional outputs',
        description='Save FastQ files after merging re-sequenced libraries in the results directory.',
    ),
    'save_umi_intermeds': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='If this option is specified, intermediate FastQ and BAM files produced by UMI-tools are also saved in the results directory.',
    ),
    'save_non_ribo_reads': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='If this option is specified, intermediate FastQ files containing non-rRNA reads will be saved in the results directory.',
    ),
    'save_bbsplit_reads': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='If this option is specified, FastQ files split by reference will be saved in the results directory.',
    ),
    'save_reference': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='If generated by the pipeline save the STAR index in the results directory.',
    ),
    'save_trimmed': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Save the trimmed FastQ files in the results directory.',
    ),
    'save_align_intermeds': NextflowParameter(
        type=typing.Optional[bool],
        default=True,
        section_title=None,
        description='Save the intermediate BAM files from the alignment step.',
    ),
    'save_unaligned': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Where possible, save unaligned reads from either STAR, HISAT2 or Salmon to the results directory.',
    ),
    'skip_gtf_filter': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title='Process skipping options',
        description='Skip filtering of GTF for valid scaffolds and/ or transcript IDs.',
    ),
    'skip_gtf_transcript_filter': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description="Skip the 'transcript_id' checking component of the GTF filtering script used in the pipeline.",
    ),
    'skip_bbsplit': NextflowParameter(
        type=typing.Optional[bool],
        default=True,
        section_title=None,
        description='Skip BBSplit for removal of non-reference genome reads.',
    ),
    'skip_umi_extract': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Skip the UMI extraction from the read in case the UMIs have been moved to the headers in advance of the pipeline run.',
    ),
    'skip_trimming': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Skip the adapter trimming step.',
    ),
    'skip_alignment': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Skip all of the alignment-based processes within the pipeline.',
    ),
    'skip_markduplicates': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Skip picard MarkDuplicates step.',
    ),
    'skip_fastqc': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Skip FastQC.',
    ),
    'skip_multiqc': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Skip MultiQC.',
    ),
    'skip_qc': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Skip all QC steps except for MultiQC.',
    ),
    'skip_ribotish': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Skip Ribo-TISH.',
    ),
    'skip_ribotricer': NextflowParameter(
        type=typing.Optional[bool],
        default=None,
        section_title=None,
        description='Skip Riboricer.',
    ),
    'multiqc_methods_description': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title='Generic options',
        description='Custom MultiQC yaml file containing HTML including a methods description.',
    ),
}

