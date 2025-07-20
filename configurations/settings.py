from loggingg import codelogger
import os

Prod = True                             


# Log file to be imported to store logs
logger = codelogger.logging_system('acg.log','ACG')       #file, projectid


video_path_file = "Video/"
Ok_path_file = "/Outputs/Annoted/OK/"
notOk_path_file = "/Outputs/Annoted/NotOK/"

os.makedirs(os.getcwd()+"/Outputs/Annoted", exist_ok=True)


