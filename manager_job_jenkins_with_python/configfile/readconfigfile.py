from unipath import Path
from functools import wraps
from os.path import expanduser
import sys
import os
import anyconfig


def config(config_key):
    def _json(func):
        @wraps(func)
        def __json(*args, **kwargs):
            #TODO: melhorar a busca pelo artefato .json
            default_file = os.getcwd() + '/configfile/config.json'
            data = anyconfig.load(default_file)

            keys = config_key.split('/')
            for key in keys:
                data = data.get(key, {})

            return func(data, *args, **kwargs)

        return __json
    return _json



"""
Classe responsavel por recuperar os dados de acesso do arquivo .json
"""
class GetConfig:
    @config('jenkinsserver')
    def get_urljenkins(jenkinsserver):
      return jenkinsserver

    @config('userinfo/token')
    def get_userinfo_token(token):
      return token

    @config('userinfo/email')
    def get_userinfo_email(email):
      return email

    @config('jobsurl/provliga/urlprovamb-liga')
    def get_jobs_info_provamb_liga(urlliga):
      return urlliga

    @config('jobsurl/provdes/urlprovamb-desliga')
    def get_jobs_info_provamb_desliga(urldesliga):
      return urldesliga


