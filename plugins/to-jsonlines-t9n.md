# to-jsonlines-t9n

* domain(s): translation
* accepts: TranslationData

Writes prompt/output pairs in JsonLines-like JSON format. Example: { "translation": { "en": "Others have dismissed him as a joke.", "ro": "Alții l-au numit o glumă." } }

```
usage: to-jsonlines-t9n [-h] [-l {DEBUG,INFO,WARN,ERROR,CRITICAL}] -o OUTPUT

Writes prompt/output pairs in JsonLines-like JSON format. Example: {
"translation": { "en": "Others have dismissed him as a joke.", "ro": "Alții
l-au numit o glumă." } }

optional arguments:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARN,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARN,ERROR,CRITICAL}
                        The logging level to use (default: WARN)
  -o OUTPUT, --output OUTPUT
                        Path of the JsonLines file to write (directory when
                        processing multiple files) (default: None)
```