import os
import json
import logging
from logging import handlers
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler
from colorama import Fore

class logging_system:
    def __init__(self, logFile, projectid = ' ', submoduleid = ' ',
                       uniquevalue = ' ', host = ' ', port = ' ',
                       technicalmodulename = 'PYTHON', processid = ' ',
                       parentprocesstag = ' ', selfprocesstag = ' ', log_type = 'APPLOG',
                       tag = ' ', endpoint = ' ', _messageI = ' ', logfolder = 'logs'):

        self.logFile             = logFile
        self.projectid           = projectid
        self.submoduleid         = submoduleid
        self.uniquevalue         = uniquevalue
        self.host                = host
        self.port                = port
        self.technicalmodulename = technicalmodulename
        self.processid           = processid
        self.parentprocesstag    = parentprocesstag
        self.selfprocesstag      = selfprocesstag
        self.type                = log_type
        self.tag                 = tag
        self.endpoint            = endpoint
        self.logFolder           = logfolder
        self._messageI           = _messageI

        self.logpath = self.logFolder + '/' + self.logFile.split(".", 1)[0]
        Path(self.logpath).mkdir(parents=True, exist_ok=True)

        self.extra = {"projectid"           : self.projectid,   # DEEPSIGHT
                      "submoduleid"         : self.submoduleid, # SIDE
                      "uniquevalue"         : self.uniquevalue, # ASSET ID
                      "host"                : self.host,        # MACHINE REGISTRATION ID
                      "port"                : self.port,        # -
                      "technicalmodulename" : self.technicalmodulename, # PYTHON
                      "processid"           : self.processid,   # TIMESTAMP
                      "parentprocesstag"    : self.parentprocesstag,    # PREDEFINED TAGS IN CONFIG
                      "selfprocesstag"      : self.selfprocesstag,      # PREDEFINED TAGS IN CONFIG
                      "type"                : self.type,        # APPLOG / SYSLOG
                      "tag"                 : self.tag,         # FILE RUNNING CODE - FUNCTION
                      "endpoint"            : self.endpoint,    # - 
                      "_messageI"           : self._messageI
                     }
        self._logs(logging.INFO)

    def _update(self,):
        self.extra = {"projectid"           : self.projectid,
                      "submoduleid"         : self.submoduleid,
                      "uniquevalue"         : self.uniquevalue,
                      "host"                : self.host,
                      "port"                : self.port,
                      "technicalmodulename" : self.technicalmodulename,
                      "processid"           : self.processid,
                      "parentprocesstag"    : self.parentprocesstag,
                      "selfprocesstag"      : self.selfprocesstag,
                      "type"                : self.type,
                      "tag"                 : self.tag,
                      "endpoint"            : self.endpoint,
                      "_messageI"           : self._messageI
                     }

    def set_submoduleid(self, new_value):
        self.submoduleid = new_value
        self._update()

    def set_uniquevalue(self, new_value):
        self.uniquevalue = new_value
        self._update()

    def set_host(self, new_value):
        self.host = new_value
        self._update()

    def set_port(self, new_value):
        self.port = new_value
        self._update()

    def set_technicalmodulename(self, new_value):
        self.technicalmodulename = new_value
        self._update()

    def set_processid(self, new_value):
        self.processid = new_value
        self._update()

    def set_parentprocesstag(self, new_value):
        self.parentprocesstag = new_value
        self._update()

    def set_selfprocesstag(self, new_value):
        self.selfprocesstag = new_value
        self._update()

    def set_type(self, new_value):
        self.type = new_value
        self._update()
            
    def set_tag(self, new_value):
        self.tag = new_value
        self._update()
            
    def set_endpoint(self, new_value):
        self.endpoint = new_value
        self._update()

    def _logs(self, log_level):
        logger = logging.getLogger(self.logFile.split(".")[0])
        #logger.setLevel(logging.INFO)
        
        formatter = logging.Formatter('%(asctime)s|%(projectid)s|%(technicalmodulename)s|' + 
                                      '%(host)s|%(port)s|%(type)s|' + 
                                      '%(levelname)s|%(tag)s|%(endpoint)s|' + 
                                      '%(uniquevalue)s|%(submoduleid)s|' +
                                      '%(processid)s|%(parentprocesstag)s|%(selfprocesstag)s|%(message)s')
                                      
        formatter.default_msec_format = '%s.%03d'

        filepath = self.logpath + '/' + self.logFile
        hdlr = TimedRotatingFileHandler(filepath,
                                    when="midnight",
                                    backupCount=90,
                                    interval=1,
                                    encoding=None,
                                    delay=0)

        #hdlr.doRollover()
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        self.logger = logger

    def info(self, message):
        print(message)
        logger = logging.LoggerAdapter(self.logger, self.extra)
        logger.setLevel(logging.INFO)
        logger.info(message)

    def debug(self, message):
        print(message)
        logger = logging.LoggerAdapter(self.logger, self.extra)
        logger.setLevel(logging.DEBUG)
        logger.debug(message)

    def warning(self, message):
        print(message)
        logger = logging.LoggerAdapter(self.logger, self.extra)
        logger.setLevel(logging.WARNING)
        logger.warning(message)

    def error(self, message):
        logger = logging.LoggerAdapter(self.logger, self.extra)
        logger.setLevel(logging.ERROR)
        logger.error(message)

    def consoleError(self, message, e):
        self.error(message)
        a=str(e.__traceback__.tb_frame).split(',')
        self.error(f'----Exception : {e}')
        self.error(f'----File      : {a[1]}')
        self.error(f'----Function  : {a[3][:-1].split()[1]}')
        self.error(f'----Line no   : {e.__traceback__.tb_lineno} ')
        print(Fore.RED + '----Exception :', e)
        print(Fore.RED + '----File      :', a[1])
        print(Fore.RED + '----Function  :', a[3][:-1].split()[1])
        print(Fore.RED + '----Line no   : ', e.__traceback__.tb_lineno, Fore.RESET)

    