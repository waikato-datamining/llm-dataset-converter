# llm-dataset-converter
For converting large language model (LLM) datasets from one format into another.
Filters can be supplied as well, e.g., for cleaning up the data.


## Installation

Via PyPI:

```bash
pip install llm-dataset-converter
```

The latest code straight from the repository:

```bash
pip install git+https://github.com/waikato-llm/llm-dataset-converter.git
```

## Docker

[Docker](docker) images are available from:

* Docker hub: [waikatodatamining/llm-dataset-converter](https://hub.docker.com/r/waikatodatamining/llm-dataset-converter)
* In-house registry: `public.aml-repo.cms.waikato.ac.nz:443/tools/llm-dataset-converter`


## Datasets

The following repository contains a curated list of datasets for LLMs:

https://github.com/Zjh-819/LLMDataHub

The Hugging Face Hub has an abundance of datasets as well:

https://huggingface.co/datasets


## Dataset formats

The following dataset formats are supported:

| Domain         | Format                                                                    | Read                                                | Write                                           | Compression |
|:---------------|:--------------------------------------------------------------------------|:----------------------------------------------------|:------------------------------------------------| :---:       |
| classification | CSV                                                                       | [from-csv-cl](plugins/from-csv-cl.md)               | [to-csv-cl](plugins/to-csv-cl.md)               | Y |
| classification | [Jsonlines](https://jsonlines.org/)                                       | [from-jsonlines-cl](plugins/from-jsonlines-cl.md)   | [to-jsonlines-cl](plugins/to-jsonlines-cl.md)   | Y |
| classification | [Parquet](https://arrow.apache.org/docs/python/parquet.html)              | [from-parquet-cl](plugins/from-parquet-cl.md)       | [to-parquet-cl](plugins/to-parquet-cl.md)       | N |    
| classification | TSV                                                                       | [from-tsv-cl](plugins/from-tsv-cl.md)               | [to-tsv-cl](plugins/to-tsv-cl.md)               | Y |
| pairs          | [Alpaca](https://github.com/tatsu-lab/stanford_alpaca#data-release)       | [from-alpaca](plugins/from-alpaca.md)               | [to-alpaca](plugins/to-alpaca.md)               | Y |    
| pairs          | CSV                                                                       | [from-csv-pr](plugins/from-csv-pr.md)               | [to-csv-pr](plugins/to-csv-pr.md)               | Y |
| pairs          | [Jsonlines](https://jsonlines.org/)                                       | [from-jsonlines-pr](plugins/from-jsonlines-pr.md)   | [to-jsonlines-pr](plugins/to-jsonlines-pr.md)   | Y |
| pairs          | [Parquet](https://arrow.apache.org/docs/python/parquet.html)              | [from-parquet-pr](plugins/from-parquet-pr.md)       | [to-parquet-pr](plugins/to-parquet-pr.md)       | N |    
| pairs          | TSV                                                                       | [from-tsv-pr](plugins/from-tsv-pr.md)               | [to-tsv-pr](plugins/to-tsv-pr.md)               | Y |
| pairs          | [XTuner](https://github.com/InternLM/xtuner/blob/v0.1.13/docs/en/user_guides/dataset_format.md#single-turn-dialogue-dataset-format)                                                                | [from-xtuner](plugins/from-xtuner.md)               | [to-xtuner](plugins/to-xtuner.md)               | Y |
| pretrain       | CSV                                                                       | [from-csv-pt](plugins/from-csv-pt.md)               | [to-csv-pt](plugins/to-csv-pt.md)               | Y |
| pretrain       | [Jsonlines](https://jsonlines.org/)                                       | [from-jsonlines-pt](plugins/from-jsonlines-pt.md)   | [to-jsonlines-pt](plugins/to-jsonlines-pt.md)   | Y |
| pretrain       | [Parquet](https://arrow.apache.org/docs/python/parquet.html)              | [from-parquet-pt](plugins/from-parquet-pt.md)       | [to-parquet-pt](plugins/to-parquet-pt.md)       | N |    
| pretrain       | TSV                                                                       | [from-tsv-pt](plugins/from-tsv-pt.md)               | [to-tsv-pt](plugins/to-tsv-pt.md)               | Y |
| pretrain       | TXT                                                                       | [from-txt-pt](plugins/from-txt-pt.md)               | [to-txt-pt](plugins/to-txt-pt.md)               | Y <sup>1</sup> |
| translation    | CSV                                                                       | [from-csv-t9n](plugins/from-csv-t9n.md)             | [to-csv-t9n](plugins/to-csv-t9n.md)             | Y |
| translation    | [Jsonlines](https://jsonlines.org/) <sup>2</sup>                          | [from-jsonlines-t9n](plugins/from-jsonlines-t9n.md) | [to-jsonlines-t9n](plugins/to-jsonlines-t9n.md) | Y |
| translation    | [Parquet](https://arrow.apache.org/docs/python/parquet.html) <sup>3</sup> | [from-parquet-t9n](plugins/from-parquet-t9n.md)     | [to-parquet-t9n](plugins/to-parquet-t9n.md)     | N |    
| translation    | TSV                                                                       | [from-tsv-t9n](plugins/from-tsv-t9n.md)             | [to-tsv-t9n](plugins/to-tsv-t9n.md)             | Y |
| translation    | TXT                                                                       | [from-txt-t9n](plugins/from-txt-t9n.md)             | [to-txt-t9n](plugins/to-txt-t9n.md)             | Y <sup>1</sup> |

<sup>1</sup> Compression not available when concatenating content in single file.

<sup>2</sup> Format defined [here](https://github.com/huggingface/transformers/blob/main/examples/pytorch/translation/README.md).

<sup>3</sup> Translation data itself is stored as JSON dictionary.

## Compression formats

In case a format supports compression, then the following compression formats 
are automatically supported for loading/saving files:

* [bzip2](https://en.wikipedia.org/wiki/Bzip2): `.bz2`
* [gzip](https://en.wikipedia.org/wiki/Gzip): `.gz`
* [xz](https://en.wikipedia.org/wiki/XZ_Utils): `.xz`
* [zstd](https://en.wikipedia.org/wiki/Zstd): `.zst`, `.zstd`


## File encodings

Most readers offer the `--encoding` option to override the automatically determined 
file encoding, as that can be wrong due to only inspecting a fixed number of bytes.
The number of bytes of a file inspected can be influenced via the following
environment variable:

```
LDC_ENCODING_MAX_CHECK_LENGTH
```

A value of `-1` means the complete file. However, that can be very slow and a smaller
value of <1MB is recommended.



## Tools

### Dataset conversion

```
usage: llm-convert [-h|--help|--help-all|-help-plugin NAME] [-u INTERVAL]
                   [-c {None,bz2,gz,xz,zstd}]
                   [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                   reader
                   [filter [filter [...]]]
                   [writer]

Tool for converting between large language model (LLM) dataset formats.

readers:
   from-alpaca, from-csv-cl, from-csv-pr, from-csv-pt, from-csv-t9n, 
   from-jsonlines-cl, from-jsonlines-pr, from-jsonlines-pt, 
   from-jsonlines-t9n, from-parquet-cl, from-parquet-pr, 
   from-parquet-pt, from-parquet-t9n, from-tsv-cl, from-tsv-pr, 
   from-tsv-pt, from-tsv-t9n, from-txt-pt, from-txt-t9n, from-xtuner
filters:
   assemble-sentences, change-case, classification-label-map, 
   file-filter, find-substr, keyword, language, llama2-to-pairs, 
   max-length-pt, max-records, metadata, metadata-from-name, 
   pairs-to-llama2, pairs-to-pretrain, 
   pretrain-sentences-to-classification, pretrain-sentences-to-pairs, 
   randomize-records, record-files, record-window, remove-blocks, 
   remove-empty, remove-patterns, replace-patterns, require-languages, 
   reset-ids, sentences-pt, skip-duplicate-ids, skip-duplicate-text, 
   split, split-pt, tee, text-length, text-stats, to-llama2-format, 
   translation-to-pairs, translation-to-pretrain, update-pair-data
writers:
   to-alpaca, to-csv-cl, to-csv-pr, to-csv-pt, to-csv-t9n, 
   to-jsonlines-cl, to-jsonlines-pr, to-jsonlines-pt, to-jsonlines-t9n, 
   to-parquet-cl, to-parquet-pr, to-parquet-pt, to-parquet-t9n, 
   to-tsv-cl, to-tsv-pr, to-tsv-pt, to-tsv-t9n, to-txt-pt, to-txt-t9n, 
   to-xtuner

optional arguments:
  -h, --help              show basic help message and exit
  --help-all              show basic help message plus help on all plugins and exit
  --help-plugin NAME      show help message for plugin NAME and exit
  -u INTERVAL, --update_interval INTERVAL
                          outputs the progress every INTERVAL records (default: 1000)
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                          the logging level to use (default: WARN)
  -c {None,bz2,gz,xz,zstd}, --compression {None,bz2,gz,xz,zstd}
                          the type of compression to use when only providing an output
                          directory to the writer (default: None)
  -b, --force_batch       processes the data in batches
  -U, --unescape_unicode  unescape unicode characters in the command-line
```

### Download

```
usage: llm-download [-h|--help|--help-all|-help-plugin NAME]
                    downloader

Tool for downloading data for large language models (LLMs).

downloaders:
   huggingface

optional arguments:
  -h, --help            show basic help message and exit
  --help-all            show basic help message plus help on all plugins and exit
  --help-plugin NAME    show help message for plugin NAME and exit
```

### Combining multiple files (one-after-the-other)

```
usage: llm-append [-h] [-i [INPUT [INPUT ...]]]
                  [-I [INPUT_LIST [INPUT_LIST ...]]]
                  [-t {csv,json,jsonlines,plain-text,tsv}] [-o FILE] [-p]
                  [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]

Tool for combining multiple text files by appending them.

optional arguments:
  -h, --help            show this help message and exit
  -i [INPUT [INPUT ...]], --input [INPUT [INPUT ...]]
                        Path to the text file(s) to append; glob syntax is
                        supported (default: None)
  -I [INPUT_LIST [INPUT_LIST ...]], --input_list [INPUT_LIST [INPUT_LIST ...]]
                        Path to the text file(s) listing the data files to
                        append (default: None)
  -t {csv,json,jsonlines,plain-text,tsv}, --file_type {csv,json,jsonlines,plain-text,tsv}
                        The type of files that are being processed. (default:
                        plain-text)
  -o FILE, --output FILE
                        The path of the file to store the combined data in;
                        outputs it to stdout if omitted or a directory
                        (default: None)
  -p, --pretty_print    Whether to output the JSON in more human-readable
                        format. (default: False)
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
```

### Combining multiple files (side-by-side)

```
usage: llm-paste [-h] [-i [INPUT [INPUT ...]]]
                 [-I [INPUT_LIST [INPUT_LIST ...]]] [-o FILE]
                 [-s [SEP [SEP ...]]] [-l {DEBUG,INFO,WARN,ERROR,CRITICAL}]

Tool for combining multiple text files by placing them side-by-side.

optional arguments:
  -h, --help            show this help message and exit
  -i [INPUT [INPUT ...]], --input [INPUT [INPUT ...]]
                        Path to the text file(s) to combine; glob syntax is
                        supported (default: None)
  -I [INPUT_LIST [INPUT_LIST ...]], --input_list [INPUT_LIST [INPUT_LIST ...]]
                        Path to the text file(s) listing the data files to
                        combine (default: None)
  -o FILE, --output FILE
                        The path of the file to store the combined data in;
                        outputs it to stdout if omitted or a directory
                        (default: None)
  -s [SEP [SEP ...]], --separator [SEP [SEP ...]]
                        The separators to use between the files; uses TAB if
                        not supplied; use '{T}' as placeholder for tab
                        (default: None)
  -l {DEBUG,INFO,WARN,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARN,ERROR,CRITICAL}
                        The logging level to use (default: WARN)
```


### File encodings

The following tool allows you to determine the encoding of text files.

```
usage: llm-file-encoding [-h] [-i [INPUT [INPUT ...]]]
                         [-I [INPUT_LIST [INPUT_LIST ...]]]
                         [-m MAX_CHECK_LENGTH] [-o FILE]
                         [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]

Tool for determining the file encoding of text files.

optional arguments:
  -h, --help            show this help message and exit
  -i [INPUT [INPUT ...]], --input [INPUT [INPUT ...]]
                        Path to the text file(s) to check; glob syntax is
                        supported (default: None)
  -I [INPUT_LIST [INPUT_LIST ...]], --input_list [INPUT_LIST [INPUT_LIST ...]]
                        Path to the text file(s) listing the actual files to
                        check (default: None)
  -m MAX_CHECK_LENGTH, --max_check_length MAX_CHECK_LENGTH
                        The maxmimum number of bytes to use for checking
                        (default: None)
  -o FILE, --output FILE
                        The path of the file to store the determined encodings
                        in; outputs it to stdout if omitted or a directory
                        (default: None)
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
```


### Locating files

Readers tend to support input via file lists. The `llm-find` tool can generate
these.

```
usage: llm-find [-h] -i DIR [DIR ...] [-r] -o FILE [-m [REGEXP [REGEXP ...]]]
                [-n [REGEXP [REGEXP ...]]]
                [--split_ratios [SPLIT_RATIOS [SPLIT_RATIOS ...]]]
                [--split_names [SPLIT_NAMES [SPLIT_NAMES ...]]]
                [--split_name_separator SPLIT_NAME_SEPARATOR]
                [-l {DEBUG,INFO,WARN,ERROR,CRITICAL}]

Tool for locating files in directories that match certain patterns and store
them in files.

optional arguments:
  -h, --help            show this help message and exit
  -i DIR [DIR ...], --input DIR [DIR ...]
                        The dir(s) to scan for files. (default: None)
  -r, --recursive       Whether to search the directories recursively
                        (default: False)
  -o FILE, --output FILE
                        The file to store the located file names in (default:
                        None)
  -m [REGEXP [REGEXP ...]], --match [REGEXP [REGEXP ...]]
                        The regular expression that the (full) file names must
                        match to be included (default: None)
  -n [REGEXP [REGEXP ...]], --not-match [REGEXP [REGEXP ...]]
                        The regular expression that the (full) file names must
                        match to be excluded (default: None)
  --split_ratios [SPLIT_RATIOS [SPLIT_RATIOS ...]]
                        The split ratios to use for generating the splits
                        (int; must sum up to 100) (default: None)
  --split_names [SPLIT_NAMES [SPLIT_NAMES ...]]
                        The split names to use as filename suffixes for the
                        generated splits (before .ext) (default: None)
  --split_name_separator SPLIT_NAME_SEPARATOR
                        The separator to use between file name and split name
                        (default: -)
  -l {DEBUG,INFO,WARN,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARN,ERROR,CRITICAL}
                        The logging level to use (default: WARN)
```


### Generating help screens for plugins

```
usage: llm-help [-h] [-c [PACKAGE [PACKAGE ...]]] [-e EXCLUDED_CLASS_LISTERS]
                [-p NAME] [-f FORMAT] [-L INT] [-o PATH] [-i FILE]
                [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]

Tool for outputting help for plugins in various formats.

optional arguments:
  -h, --help            show this help message and exit
  -c [PACKAGE [PACKAGE ...]], --custom_class_listers [PACKAGE [PACKAGE ...]]
                        The names of the custom class listers, uses the
                        default ones if not provided. (default: None)
  -e EXCLUDED_CLASS_LISTERS, --excluded_class_listers EXCLUDED_CLASS_LISTERS
                        The comma-separated list of class listers to excluded.
                        (default: None)
  -p NAME, --plugin_name NAME
                        The name of the plugin to generate the help for,
                        generates it for all if not specified (default: None)
  -f FORMAT, --help_format FORMAT
                        The output format to generate (default: text)
  -L INT, --heading_level INT
                        The level to use for the heading (default: 1)
  -o PATH, --output PATH
                        The directory or file to store the help in; outputs it
                        to stdout if not supplied; if pointing to a directory,
                        automatically generates file name from plugin name and
                        help format (default: None)
  -i FILE, --index FILE
                        The file in the output directory to generate with an
                        overview of all plugins, grouped by type (in markdown
                        format, links them to the other generated files)
                        (default: None)
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
```


### Plugin registry

```
usage: llm-registry [-h] [-c CUSTOM_CLASS_LISTERS] [-e EXCLUDED_CLASS_LISTERS]
                    [-l {plugins,custom-class-listers,env-class-listers,downloaders,readers,filters,writers}]

For inspecting/querying the registry.

optional arguments:
  -h, --help            show this help message and exit
  -c CUSTOM_CLASS_LISTERS, --custom_class_listers CUSTOM_CLASS_LISTERS
                        The comma-separated list of custom class listers to
                        use. (default: None)
  -e EXCLUDED_CLASS_LISTERS, --excluded_class_listers EXCLUDED_CLASS_LISTERS
                        The comma-separated list of class listers to excluded.
                        (default: None)
  -l {plugins,custom-class-listers,env-class-listers,downloaders,readers,filters,writers}, --list {plugins,custom-class-listers,env-class-listers,downloaders,readers,filters,writers}
                        For outputting various lists on stdout. (default:
                        None)
```


## Plugins

See [here](plugins/README.md) for an overview of all plugins.


## Command-line examples

Use the [alpaca_data_cleaned.json](https://github.com/gururise/AlpacaDataCleaned/blob/main/alpaca_data_cleaned.json)
dataset for the following examples.

### Conversion

```bash
llm-convert \
  from-alpaca \
    --input ./alpaca_data_cleaned.json \
  to-csv-pr \
    --output alpaca_data_cleaned.csv
```

If you want some logging output, e.g., on progress and what files are being 
processed/generated:

```bash
llm-convert \
  -l INFO \
  from-alpaca \
    --input ./alpaca_data_cleaned.json \
    -l INFO \
  to-csv-pr \
    --output alpaca_data_cleaned.csv
    -l INFO
```

### Compression

The output gets automatically compressed (when the format supports that), based
on the extension that you use for the output.

The following uses Gzip to compress the CSV file:

```bash
llm-convert \
  from-alpaca \
    --input ./alpaca_data_cleaned.json \
  to-csv-pr \
    --output alpaca_data_cleaned.csv.gz
```

The input gets automatically decompressed based on its extension, provided 
the format supports that.

### Processing multiple files

Provided that the reader supports, you can also process multiple files, one
after the other. For that you either specify them explicitly (multiple 
arguments to the `--input` option) or use a glob syntax (e.g., `--input "*.json"`).
For the latter, you should surround the argument with double quotes to avoid
the shell expanding the names automatically.

If you have a lot of files, it will be more efficient to store these in text
files (with one file per line) and pass these to the reader using the 
`--input_list` option (assuming that the reader supports this). Such file
lists can be generated with the `llm-find` tool. See below `Locating files`.

As for specifying the output, you simply specify the output directory. An output
file name gets automatically generated from the name of the current input file
that is being processed.

If you want to compress the output files, you need to specify your preferred
compression format via the global `-c/--compression` option of the `llm-convert`
tool. By default, no compression is used.

Please note, that when using a *stream writer* (e.g., for text or jsonlines 
output) in conjunction with an output directory, each record will be stored 
in a separate file. In order to transfer all the records into a single file, 
you have to explicitly specify that file as output.

### Filtering

Instead of just reading and writing the data records, you can also inject
filters in between them. E.g., the following command-line will load the
Alpaca JSON dataset and only keep records that have the keyword `function`
in either the `instruction`, `input` or `output` data of the record:

```bash
llm-convert \
  -l INFO \
  from-alpaca \
    -l INFO \
    --input alpaca_data_cleaned.json \
  keyword \
    -l INFO \
    --keyword function \
    --location any \
    --action keep \
  to-alpaca \
    -l INFO \
    --output alpaca_data_cleaned-filtered.json 
```

**NB:** When chaining filters, the tool checks whether accepted input and 
generated output is compatible (including from reader/writer).

### Download

The following command downloads the file `vocab.json` from the Hugging Face
project [lysandre/arxiv-nlp](https://huggingface.co/lysandre/arxiv-nlp):

```bash
llm-download \
  huggingface \
  -l INFO \
  -i lysandre/arxiv-nlp \
  -f vocab.json \
  -o .
```

The next command gets the file `part_1_200000.parquet` from the dataset
[nampdn-ai/tiny-codes](https://huggingface.co/datasets/nampdn-ai/tiny-codes) 
(if you don't specify a filename, the complete dataset will get downloaded):

```bash
llm-download \
  huggingface \
  -l INFO \
  -i nampdn-ai/tiny-codes \
  -t dataset \
  -f part_1_200000.parquet \
  -o .
```

**NB:** Hugging Face will cache files locally in your home directory before
copying it to the location that you specified.


### Locating files

The following command scans the `/some/dir` directory recursively for `.txt`
files that do not have `raw` in the file path:

```
llm-find \
    -l INFO \
    -i /some/dir/
    -r \
    -m ".*\.txt" \
    -n ".*\/raw\/.*" \
    -o ./files.txt
```

The same command, but splitting the files into training, validation and test 
lists, using a ratio of 70/15/15:

```
llm-find \
    -l INFO \
    -i /some/dir/
    -r \
    -m ".*\.txt" \
    -n ".*\/raw\/.*" \
    --split_ratios 70 15 15 \
    --split_names train val test \
    -o ./files.txt
```

This results in the following three files: `files-train.txt`, `files-val.txt` 
and `files-test.txt`.


## Code example

Of course, you can use the library also from Python itself.

The following code sets up a pipeline that reads in a prompt/response 
dataset in Alpaca format, filters out records that do not contain the 
keyword `function` anywhere in the record, converts it to *pretrain* data
and then outputs it in zstandard-compressed jsonlines format:

```python
from wai.logging import LOGGING_INFO, init_logging
from seppl.io import execute
from ldc.api.supervised.pairs import PAIRDATA_FIELDS
from ldc.core import Session, ENV_LLM_LOGLEVEL
from ldc.api import COMPRESSION_ZSTD
from ldc.registry import register_plugins
from ldc.supervised.pairs import AlpacaReader
from ldc.pretrain import JsonLinesPretrainWriter
from ldc.filter import PairsToPretrain, Keyword

init_logging(env_var=ENV_LLM_LOGLEVEL)
register_plugins()

execute(
    AlpacaReader(
        source="./alpaca_data_cleaned.json",
        logging_level=LOGGING_INFO
    ),
    [
        Keyword(
            keywords=["function"],
            logging_level=LOGGING_INFO
        ),
        PairsToPretrain(
            data_fields=PAIRDATA_FIELDS
        ),
    ],
    JsonLinesPretrainWriter(
        target="./output",
        att_content="text",
        logging_level=LOGGING_INFO
    ),
    Session()
        .set_logging_level(LOGGING_INFO)
        .set_compression(COMPRESSION_ZSTD),
)
```


## Additional libraries

* [Google integration](https://github.com/waikato-llm/ldc-google)
* [HTML handling](https://github.com/waikato-llm/ldc-html)
* [MS Word .docx integration](https://github.com/waikato-llm/ldc-docx)
* [OpenAI integration](https://github.com/waikato-llm/ldc-openai)
* [PDF handling](https://github.com/waikato-llm/ldc-pdf)
* [TinT](https://github.com/waikato-llm/ldc-tint)


## Class listers

The *llm-dataset-converter* uses the *class lister registry* provided 
by the [seppl](https://github.com/waikato-datamining/seppl) library.

Each module defines a function, typically called `list_classes` that returns
a dictionary of names of superclasses associated with a list of modules that
should be scanned for derived classes. Here is an example:

```python
from typing import List, Dict


def list_classes() -> Dict[str, List[str]]:
    return {
        "ldc.api.Downloader": [
            "mod.ule1",
        ],
        "ldc.api.Reader": [
            "mod.ule2",
            "mod.ule3",
        ],
        "ldc.api.Filter": [
            "mod.ule4",
        ],
        "seppl.io.Writer": [
            "mod.ule5",
        ],
    }
```

Such a class lister gets referenced in the `entry_points` section of the `setup.py` file:

```python
    entry_points={
        "class_lister": [
            "unique_string=module_name:function_name",
        ],
    },
```

`:function_name` can be omitted if `:list_classes`.

The following environment variables can be used to influence the class listers:

* `LDC_CLASS_LISTERS`
* `LDC_CLASS_LISTERS_EXCL`

Each variable is a comma-separated list of `module_name:function_name`, defining the class listers.
