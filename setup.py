from setuptools import setup, find_packages
setup(
    name = "skat_utilities",
    version = "0.1",
    packages =['skat_util'],
    author="James Boocock",
    author_email="james.boocock@otago.ac.nz",
    description="SKAT utilities (for rare variant testing)",
    entry_points = {
        'console_scripts' : [
            'anno_gene_to_skat = skat_util.gene_annotation_to_SSID:main'
        ]
    },
    url="https://github.com/smilefreak/skat_utilities"
)


    
