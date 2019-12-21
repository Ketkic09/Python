import logging 
#creating log and logformat
LOG_FORMAT = " %(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "C:\\Users\\ketki\\Assignments\\assgn1\\testlog.log", level = logging.DEBUG, format = LOG_FORMAT,filemode='a')
#basicConfig is a method in logging dir
#level is set to debug

#creating an obj
lg = logging.getLogger()
#writing a msg in log
lg.info("First message")
#there are diff levels in py each having a int val. default val is set to warning - 30
#only the value >= is stored in log 

#level wise msg
x = input("Enter message")
lg.info(x)
