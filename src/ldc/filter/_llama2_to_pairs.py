from typing import List

from wai.logging import LOGGING_WARNING
from ldc.core import DOMAIN_PAIRS, DOMAIN_PRETRAIN
from ldc.api.pretrain import PretrainData
from ldc.api.supervised.pairs import PairData
from ldc.api import Filter


class Llama2ToPairs(Filter):
    """
    Converts llama2 pretrain records to prompt/response pairs.

    <s>[INST] <<SYS>>
    {{system message}}
    <</SYS>>
    {{message}} [/INST] {{answer}} </s>

    <s>[INST] {{message}} [/INST] {{answer}} </s>

    <s>[INST] {{message}} [/INST]
    """

    def __init__(self, logger_name: str = None, logging_level: str = LOGGING_WARNING):
        """
        Initializes the filter.

        :param logger_name: the name to use for the logger
        :type logger_name: str
        :param logging_level: the logging level to use
        :type logging_level: str
        """
        super().__init__(logger_name=logger_name, logging_level=logging_level)

    def name(self) -> str:
        """
        Returns the name of the handler, used as sub-command.

        :return: the name
        :rtype: str
        """
        return "llama2-to-pairs"

    def description(self) -> str:
        """
        Returns a description of the handler.

        :return: the description
        :rtype: str
        """
        return "Converts llama2 pretrain records to prompts/response ones. " \
               + "The 'instruction' (ie prompt) is extracted from [INST]...[/INST] " \
               + "and the 'output' (ie response) is the string that follows the [/INST]. " \
               + "Splits on <s> to generate multiple prompt/response records."

    def domains(self) -> List[str]:
        """
        Returns the domains of the handler.

        :return: the domains
        :rtype: list
        """
        return [DOMAIN_PAIRS, DOMAIN_PRETRAIN]

    def accepts(self) -> List:
        """
        Returns the list of classes that are accepted.

        :return: the list of classes
        :rtype: list
        """
        return [PretrainData]

    def generates(self) -> List:
        """
        Returns the list of classes that get produced.

        :return: the list of classes
        :rtype: list
        """
        return [PairData]

    def _do_process(self, data: PretrainData):
        """
        Processes the data record.

        :param data: the record to process
        :type data: PairData
        :return: the potentially updated record(s)
        """
        result = []

        s = data.content
        s = s.replace("\r", " ")
        if "<s>" in s:
            s = data.content.strip()
            if s.startswith("<s>"):
                s = s[3:].strip()
            items = s.replace("<s>", "\b").split("\b")
        else:
            items = [s]

        for item in items:
            instruction = None
            output = None
            item = item.replace("</s>", "").replace("[INST]", "\r").replace("[/INST]", "\b")
            if ("\r" in item) and ("\b" in item):
                instruction = item[item.index("\r")+1:item.index("\b")].strip()
                output = item[item.index("\b")+1:].strip()
            if (instruction is not None) and (output is not None):
                result.append(PairData(instruction=instruction, output=output, input=None))

        if len(result) == 1:
            result = result[0]
        return result
