#!/usr/bin/env/python
"""Using the file system load."""
import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Capture our current directory
DIR = os.path.dirname(os.path.abspath(__file__))

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

plot = figure()
plot.circle([1, 2], [3, 4])
HTML = file_html(plot, CDN, "my plot")


def compile_jinja_template(template, context, export=True):
    """
    Create the jinja2 environment.

    Notice the use of trim_blocks, which greatly helps control whitespace.
    """
    j2_env = Environment(loader=FileSystemLoader(DIR), trim_blocks=False)
    rendered_html = j2_env.get_template(str(template)).render(**context)
    if export:
        with open(Path("outfiles", template.stem), "w") as outfile:
            outfile.write(rendered_html)
    else:
        print(rendered_html)


if __name__ == "__main__":
    with open("example.data", "r") as image_file:
        IMAGE = image_file.read()

    CONTEXT = {
        "title": "Oh my God !!",
        "individual": {
            "system_id": "IID_H108333",
            "gender": "MALE",
            "custom_fields": {"germline_consent": "True", "dmp_id": "P-0006237"},
        },
        "samples": [
            {
                "system_id": "I-H-108333-T01",
                "sample_class": "TUMOR",
                "disease": {
                    "acronym": "UNDIFS",
                    "name": "UNDIFFERENTIATED SARCOMA",
                    "slug": "UNDIFFERENTIATED SARCOMA (UNDIFS)",
                },
            },
            {
                "system_id": "I-H-108333-T01",
                "sample_class": "TUMOR",
                "disease": {
                    "acronym": "UNDIFS",
                    "name": "EDWIG SARCOMA",
                    "slug": "EDWIG SARCOMA (EWS)",
                },
            },
        ],
        "experiments": [
            {
                "system_id": "I-H-108333-T01-1-D1-1",
                "sample": "I-H-108333-T01",
                "technique": {"analyte": "DNA", "method": "WG"},
            },
            {
                "system_id": "I-H-108333-T01-1-R1-1",
                "sample": "I-H-108333-T01",
                "technique": {"analyte": "RNA", "method": "WT"},
            },
        ],
        "results": [
            {
                "title": "CBio Portal Results",
                "id": "cbio-portal-results",
                "data": {
                    "datatable": {
                        "headers": [
                            {"name": "Tumor_Sample_Barcode"},
                            {"name": "Chromosome"},
                            {"name": "Start_Position"},
                            {"name": "Reference_Allele"},
                            {"name": "Tumor_Seq_Allele2"},
                            {"name": "Hugo_Symbol"},
                            {"name": "VAF"},
                            {"name": "Variant_Classification"},
                            {"name": "HGVSp_Short"},
                        ],
                        "rows": [
                            {
                                "Tumor_Sample_Barcode": "P-0006237-T04-IM6",
                                "Chromosome": "3",
                                "Start_Position": "178917478",
                                "Reference_Allele": "G",
                                "Tumor_Seq_Allele2": "A",
                                "Hugo_Symbol": "PIK3CA",
                                "VAF": "0.270423",
                                "Variant_Classification": "Missense_Mutation",
                                "HGVSp_Short": "p.G118D",
                            }
                        ],
                    }
                },
            },
            {
                "title": "RNA Sample: I-H-108333-T2-1-R1",
                "id": "rna-sample-i-h-108333-t2-1-r1-1",
                "data": {
                    "datatable": {
                        "title": "High Confidence Fusions",
                        "headers": [
                            {"name": "GENE1"},
                            {"name": "GENE2"},
                            {"name": "DESCRIPTION"},
                            {"name": "SPAN_READS"},
                            {"name": "SPLIT_READS"},
                            {"name": "LEFTBREAK"},
                            {"name": "RIGHTBREAK"},
                            {"name": "CALLER_EFFECT"},
                            {"name": "ANNOT_EFFECT"},
                            {"name": "CALLER"},
                            {"name": "NUM_CALLERS"},
                        ],
                        "rows": [
                            {
                                "GENE1": "MGA",
                                "GENE2": "NUTM1",
                                "DESCRIPTION": "oncogene,cancer,exon-exon",
                                "SPAN_READS": "14",
                                "SPLIT_READS": "19",
                                "LEFTBREAK": "15:42054560:+",
                                "RIGHTBREAK": "15:34640170:+",
                                "CALLER_EFFECT": "in-frame",
                                "ANNOT_EFFECT": "in-frame",
                                "CALLER": "FUSIONCATCHER",
                                "NUM_CALLERS": "3",
                            },
                            {
                                "GENE1": "IGH@",
                                "GENE2": "IL3RA",
                                "DESCRIPTION": "known,cancer,m0,multi",
                                "SPAN_READS": "3",
                                "SPLIT_READS": "1",
                                "LEFTBREAK": "14:106913401:-",
                                "RIGHTBREAK": "X:1449932:+",
                                "CALLER_EFFECT": "---/intergenic",
                                "ANNOT_EFFECT": "---/intergenic",
                                "CALLER": "FUSIONCATCHER",
                                "NUM_CALLERS": "1",
                            },
                        ],
                    }
                },
                "modal": {
                    "button_text": "View Rescued Fusions",
                    "title": "Rescued Fusions",
                    "datatable": {
                        "headers": [
                            {"name": "GENE1"},
                            {"name": "GENE2"},
                            {"name": "DESCRIPTION"},
                            {"name": "SPAN_READS"},
                            {"name": "SPLIT_READS"},
                            {"name": "LEFTBREAK"},
                            {"name": "RIGHTBREAK"},
                            {"name": "CALLER_EFFECT"},
                            {"name": "ANNOT_EFFECT"},
                            {"name": "CALLER"},
                            {"name": "NUM_CALLERS"},
                        ],
                        "rows": [
                            {
                                "GENE1": "MGA",
                                "GENE2": "NUTM1",
                                "DESCRIPTION": "oncogene,cancer,exon-exon",
                                "SPAN_READS": "14",
                                "SPLIT_READS": "19",
                                "LEFTBREAK": "15:42054560:+",
                                "RIGHTBREAK": "15:34640170:+",
                                "CALLER_EFFECT": "in-frame",
                                "ANNOT_EFFECT": "in-frame",
                                "CALLER": "FUSIONCATCHER",
                                "NUM_CALLERS": "3",
                            },
                            {
                                "GENE1": "IGH@",
                                "GENE2": "IL3RA",
                                "DESCRIPTION": "known,cancer,m0,multi",
                                "SPAN_READS": "3",
                                "SPLIT_READS": "1",
                                "LEFTBREAK": "14:106913401:-",
                                "RIGHTBREAK": "X:1449932:+",
                                "CALLER_EFFECT": "---/intergenic",
                                "ANNOT_EFFECT": "---/intergenic",
                                "CALLER": "FUSIONCATCHER",
                                "NUM_CALLERS": "1",
                            },
                        ],
                    },
                },
            },
            {"title": "Fusion Results", "id": "fusion-results"},
            {
                "title": "Expression TSNE Results",
                "id": "expression-tsne-results",
                "data": {
                    "embedded": {
                        "title": "No Amplifications or Homozygous losses for Oncogenes or TSGs",
                        "img": IMAGE,
                    }
                },
            },
            {
                "title": "Overexpressed Cancer Genes",
                "id": "overexpressed-cancer-genes",
                "data": {"embedded": {"html": HTML}},
            },
            {
                "title": "WGS Sample: I-H-108333-T2-2-D1",
                "id": "wgs-sample-i-h-108333-t2-2-d1-1",
            },
            {"title": "Copy Number Results", "id": "copy-number-results"},
            {"title": "SNV Results", "id": "snv-results"},
            {"title": "Indel Results", "id": "indel-results"},
            {"title": "Rearrangement Results", "id": "rearrangement-results"},
            {"title": "Calls by Numbers", "id": "calls-by-numbers"},
            {"title": "Integrated Circos", "id": "integrated-circos"},
            {"title": "Mutational Signaturs", "id": "mutational-signatures"},
        ],
    }
    TEMPLATE = Path("templates", "index.html.jinja")
    compile_jinja_template(TEMPLATE, CONTEXT)
