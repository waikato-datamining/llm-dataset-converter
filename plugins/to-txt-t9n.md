# to-txt-t9n

* domain(s): translation
* accepts: TranslationData

Writes translation data to plain text files.
When providing an output directory, either uses the current session counter as the filename or, if present, the 'id' value from the meta-data.
When providing an output file, all incoming content will be concatenated in this one file. Compression is not available in this case due to the streaming context.

```
usage: to-txt-t9n [-h] [-l {DEBUG,INFO,WARN,ERROR,CRITICAL}] -o OUTPUT
                  [-d NUM] [-f FORMAT]

Writes translation data to plain text files. When providing an output
directory, either uses the current session counter as the filename or, if
present, the 'id' value from the meta-data. When providing an output file, all
incoming content will be concatenated in this one file. Compression is not
available in this case due to the streaming context.

optional arguments:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARN,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARN,ERROR,CRITICAL}
                        The logging level to use (default: WARN)
  -o OUTPUT, --output OUTPUT
                        Path to the directory or file to write to (default:
                        None)
  -d NUM, --num_digits NUM
                        The number of digits to use for the filenames
                        (default: 6)
  -f FORMAT, --line_format FORMAT
                        The format for the lines in the text file (default:
                        {LANG}-{ID}: {CONTENT})
```