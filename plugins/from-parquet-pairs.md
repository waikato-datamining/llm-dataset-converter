# from-parquet-pairs

* domain(s): pairs
* generates: PairData

Reads prompt/output pairs from Parquet database files.

```
usage: from-parquet-pairs [-h] [-l {DEBUG,INFO,WARN,ERROR,CRITICAL}] -i INPUT
                          [INPUT ...] [--col_instruction COL]
                          [--col_input COL] [--col_output COL]

Reads prompt/output pairs from Parquet database files.

optional arguments:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARN,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARN,ERROR,CRITICAL}
                        The logging level to use (default: WARN)
  -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                        Path to the parquet file(s) to read; glob syntax is
                        supported (default: None)
  --col_instruction COL
                        The name of the column with the instructions (default:
                        None)
  --col_input COL       The name of the column with the inputs (default: None)
  --col_output COL      The name of the column with the outputs (default:
                        None)
```