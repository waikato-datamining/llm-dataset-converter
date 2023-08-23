# keyword

* domain(s): pairs, pretrain
* accepts: PairData, PretrainData
* generates: PairData, PretrainData

Keeps or discards data records based on keyword(s).

```
usage: keyword [-h] [-l {DEBUG,INFO,WARN,ERROR,CRITICAL}] -k KEYWORD
               [KEYWORD ...] [-L {any,instruction,input,output,content}]
               [-a {keep,discard}]

Keeps or discards data records based on keyword(s).

optional arguments:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARN,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARN,ERROR,CRITICAL}
                        The logging level to use (default: WARN)
  -k KEYWORD [KEYWORD ...], --keyword KEYWORD [KEYWORD ...]
                        The keywords to look for (default: None)
  -L {any,instruction,input,output,content}, --location {any,instruction,input,output,content}
                        Where to look for the keywords; pairs:
                        any,instruction,input,output, pretrain: any,content
                        (default: any)
  -a {keep,discard}, --action {keep,discard}
                        How to react when a keyword is encountered (default:
                        keep)
```