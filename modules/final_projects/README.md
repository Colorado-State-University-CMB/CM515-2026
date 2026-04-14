# Final Projects

Submission of a final project is worth 10% of the total course grade. You are encouraged to utilize the many instructors of the course as mentors or advisors as you complete this project. 

#### For all projects, you will be evaluated on:

* Project-specific deliverables: Each suggested project has a list of deliverables
* Reproducibility: Thorough documentation in your README files and reports, and all code should be commented
* Scientific thinking: Each project expects you to propose rational explanations, critically analyze pre-existing work, or design code that considers challenges in data analysis
* Writeup: Whether your writeup is in a README or a separate document, you should write clearly with good grammar and complete thoughts
* AI usage statement: AI should not complete your entire project, but it can be used to support your work or your understanding. In every writeup, include how you used AI and to what extent.

#### Note on project scope: 
These project options vary in topic and approach, but they are all expected to represent a similar level of effort (~10-20 hrs). Students should get approval for their chosen project before beginning, which will help ensure your project is appropriately scoped. Projects will be evaluated primarily on your process, reasoning, and documentation — not on whether you reach a complete or “correct” answer.

## Project Suggestion 1: Propose your own project

If none of the suggested projects listed below fit with what you would prefer to work on, you may propose your own project goals, scope, and submission criteria for approval.

## Project Suggestion 2a: Explore a gene of unknown function

Select a gene of unknown function for a specific species. Using tools presented in class and available sequence data, reference genomes, and annotations, develop hypotheses for the possible function(s) of the selected gene (e.g. predicted structure, sequence homology, phylogenetic distribution, etc.). 

### How to select a gene

* Must be annotated as hypothetical, uncharacterized, and/or DUF (domain of unknown function)
* Must be predicted to encode a protein
* Predicted protein is not too long or too short (80-400aa?)
* The gene sequence is available in a reference genome
* Predicted structure already in AlphaFold and has some "confident" regions
* Homologs are present in other species

Here are some additional resources on how to identify an unknown gene: 
* https://fmug.amaral.northwestern.edu/
* https://dx.plos.org/10.1371/journal.pbio.3002222

### Deliverables

* Nucleotide and protein sequence files
* A GitHub repo with files containing all code you wrote related to this project
* A README for the repo
    * At a minimum, it should describe your project goals and the gene you are exploring. If you want, your entire writeup can be complied here
* Sequence analysis summary including top hits, homologs, and domain architecture (e.g. from BLAST or other database searches)
* Protein and/or RNA structure prediction (e.g. with Alphafold, etc.)
* Sequence alignment to the genome and a phylogenetic tree considering homologs of the gene
* Interpretation of all of the above, addressing any limitations you encountered, with a final hypothesis (or multiple!) of what the gene might do
* Suggestions for what experimental evidence could be collected to validate your findings
* References for any published bioinformatics tools/packages you used!
* If you come across any papers that helped you understand this particular gene, reference them as well, especially if they have their own hypothesis about the gene function

## Project Suggestion 2b: Explore a variant of unknown significance

Same basic guidelines and deliverables as above in 2a, but for a gene variant instead of a gene. Compare the most common variant(s) of the gene to your variant of interest to hypothesize significance. In this case, you may way to pick a rare variant of a gene that has a KNOWN function, to more easily discuss the potential effects.

## Project Suggestion 3: Test the reproducibility of an existing publication

Find a peer-reviewed publication online or from your lab that has some computational component (data analysis, modeling, simulation, etc.) publicly available via GitHub. Using publicly accessible data, code, and documentation, attempt to reproduce some or all of the figures or results published in the paper.

### How to select a paper

* Data should be open, accessible, processed (or very simple if raw), and not too huge to work on a laptop
* Analysis should rely on Python and/or R and standard (open source) packages/libraries
* A GitHub repo should be available for the paper to give you a starting point
* Figures may include PCA/UMAP/tSNE, violin plots, volcano plots, heatmaps, clusters, etc.

Here is an example if you want inspiration: https://github.com/deanslee/FigureOneLab/blob/main/README.md

### Deliverables

* File or link for the paper you chose
* Files or links to the data and code that come from the paper
* A GitHub repo with files containing all code YOU wrote or modified related to this project
* A README for the repo
    * At a minimum, it should describe your project goals and the paper you are exploring. If you want, your entire writeup can be complied here
* The figures/data tables you generated from the data
* A writeup that includes:
    * A summary of the scientific question being asked in the paper
    * The extent to which their data and computational methods were easily accessible
    * How easy or hard it was to locate and follow their steps
    * How well your results and/or figures match their published work
        * If your figures are different from theirs, why might that be? How might this change the conclusions they drew in their paper?
    * What the authors did well or poorly in terms of reproducibility
    * What you will do in your own projects in the future to ensure your work is rigorous and reproducible
    * References for any published bioinformatics tools/packages you used!

## Project Suggestion 4: Create a reusable data analysis pipeline

Write code in any subset of languages we've covered in class (Bash, Python, R) to perform filtering and analysis on a specific type of data (RNAseq, DNAseq, microscopy images, data tables, etc.), including the generation of at least three figures or tables that provide meaningful information about that data. You may use any tools, software, or packages available to you (whether we covered them in class or not). The code should be general enough to use on data from multiple projects, though you can make assumptions about the format of the input file(s). 

### How to define the scope of a pipeline

* Specify the type of input data you will analyze, and the expected format of the input file(s)
* Decide what question(s) your pipeline with help answer, and who might use your pipeline
* Define the output figures/tables needed to answer your question(s)
* Outline the steps needed to achieve these outputs
* Decide what pre-existing tools you can utilize (Hint: The best pipelines don't reinvent the wheel! String together known and trusted tools when you can.)

### Deliverables

* Example input data
* Example output figures/tables
* A GitHub repo with files containing all code you wrote related to this project
* A README for the repo. At a minimum, it should describe:
    * Your project goals and the goals of your pipeline
    * How to use your pipeline, including any packages that need to be installed (it's good practice to include version numbers!)
        * If your pipeline has configuration options, make sure to document that as well!
    * A brief description of the structure of your project files (folders and subfolders, purpose of the code files, where output will be stored, etc.)
    * What outputs (figures/tables/statistics) a user can expect
* Additional writeup that includes (this can be included in the README, or in a separate document):
    * A summary of your thought process when designing your pipeline, including the answers to the above questions in "How to define the scope of a pipeline"
    * A consideration of the limitaions of your pipeline (e.g. input file format, amount of data needed, limitations of the tools you utilize, run time of the pipeline, etc.)
    * A description of your experience creating a pipeline - what was challenging, what was easy, how well does it streamline the analysis of the data?
    * References to any papers that may have helped inspire your pipeline
    * References for any published bioinformatics tools/packages you used!

 ### Example Project

 I want to create a pipeline that serves to help with preliminary exploration of single-cell RNAseq data. I will need to (1) filter the reads for quality, (2) create a tSNE/UMAP plot to see how the data clusters (maybe I'll let users configure some options heres??), (3) input a metadata file to let users compare conditions with gene expression heatmaps. My output figures will be (1) a fastp report (which includes figures), (2) a tSNE or UMAP plot for clustering, and (3) a heatmap between 2 user-defined conditions. I will use a combination of BASH and R scripts. I can use a read-filtering tool such as fastp for step 1, and there are pre-existing R packages for creating the other plots I want.

## Project Suggestion 5: Explore a protein family

Use protein prediction and analysis tools to explore and summarize information about a protein family of your choice. Propose a question or set of smaller questions about the selected protein family that you could answer with publicly available data.

### How to choose a protein family

* Must have multiple members (but ideally not too many!) either across species or within a species to allow patterns to be explored
* Must have sequence data for multiple members available across databases such as NCBI, Ensembl, UniProt, or PDB
* There should be known function for at least some members of this family

### Example approaches to define questions about the protein family

* Motivated by unvalidated observations by you or others (hinted at or suggested in literature)
* Exploration of other potential proteins or molecules that interact with this family (keep the scope of this narrow!)
* Comparative questions between proteins within the family (e.g. structures, functions, expression levels, etc.)
* Comparative questions across species, cell types, tissues, etc.

### Deliverables

* Sequence alignment to reference genomes
* Phylogenetic tree construction
* Some structural prediction(s) of the protein members (e.g. with Alphafold)
* Any other figures or analyses relevant to your specific question(s)
* A GitHub repo with files containing all code you wrote related to this project
* A README for the repo
    * At a minimum, it should describe your project goals and the protein family you are exploring. If you want, your entire writeup can be complied here
* A writeup with brief background about what is known about the protein family, which questions you decided to investigate, what inspired those questions, and your methods and progress towards summarizing your findings.
    * A summary of what is currently known and published about the protein family of choice - sequence data and/or structures, known or suspected functions, how common these proteins are across taxa, etc.
    * A description of your question(s) about the protein family and why the question(s) are interesting
    * A summary of your findings, limitations, and to what degree your analyses answered your questions
    * Suggestions for what experimental evidence could be collected to validate your findings
    * References to papers you reviewed to define your questions
    * References for any published bioinformatics tools/packages you used!

## More projects may be suggested by instructors as the semester continues
