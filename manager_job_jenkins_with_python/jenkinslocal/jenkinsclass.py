import jenkins
import sys
import time
from configfile.readconfigfile import *

class JenkinsUser:
    def __init__(self):
        self.config = GetConfig
        self.jenkinsuser = jenkins.Jenkins(self.config.get_urljenkins(), username=self.config.get_userinfo_email(),
                        password=self.config.get_userinfo_token(), timeout=10)

    def ligar_instancia(self,projetojenkins,instanceID,liga):
        params = {'INSTANCE_ID': instanceID}
        if(liga):
            self.jenkinsuser.build_job(self.config.get_jobs_info_provamb_liga(),parameters=params)

    def desligar_instancia(self,projetojenkins,instanceID,desliga):
        params = {'INSTANCE_ID': instanceID}
        if (desliga):
            self.jenkinsuser.build_job(self.config.get_jobs_info_provamb_desliga(),parameters=params)

    def retornar_console_log(self):
        pass

    def checa_status_instancia(self):
        pass