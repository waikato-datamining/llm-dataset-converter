# from-parquet-pt

* domain(s): pretrain
* generates: PretrainData

Reads text from Parquet database files to use for pretraining.

```
usage: from-parquet-pt [-h] [-l {DEBUG,INFO,WARN,ERROR,CRITICAL}] -i INPUT
                       [INPUT ...] [--col_content COL] [--col_id COL]

Reads text from Parquet database files to use for pretraining.

optional arguments:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARN,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARN,ERROR,CRITICAL}
                        The logging level to use (default: WARN)
  -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                        Path to the parquet file(s) to read; glob syntax is
                        supported (default: None)
  --col_content COL     The name of the column with the text to retrieve
                        (default: None)
  --col_id COL          The name of the column with the row IDs (gets stored
                        under 'id' in meta-data) (default: None)
```