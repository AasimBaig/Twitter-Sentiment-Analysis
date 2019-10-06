import twitter
import json
import os
import re
import csv
import time


cons_key = "mNxnoZIpZYeHJV9GaM4Rz0Cwi"
cons_secret = "ooMKnp4ozpAaYE0eZpuFMcyqSqYiMolGwSMJmM97Cf3En599AA"
acc_key = "1180536763346894849-KD5UvELJbFKrshap2yjNM0aQjGKn2v"
acc_secret = "aoiBD4MUiM2136WZweraKvLac0qITelSTcmKhXSl4WGyE"

twitter_api = twitter.Api(consumer_key=cons_key,
consumer_secret=cons_secret,
access_token_key=acc_key,
access_token_secret=acc_secret)

def build_training_set(corpusfile,full_corpus):
    
