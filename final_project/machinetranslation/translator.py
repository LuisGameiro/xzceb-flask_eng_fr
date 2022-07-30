'''
translator python
'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['APIKEY']
URL = os.environ['URL']

# missing part 9
AUTHENTIFICATOR = IAMAuthenticator(APIKEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(version='2022-07-30', authenticator=AUTHENTIFICATOR)

LANGUAGE_TRANSLATOR.set_service_url(URL)


def english_to_french(english_text):
    '''function to tranlate engish to french'''
    french_text = LANGUAGE_TRANSLATOR.translate(text=english_text, model_id='en-fr').get_result()
    #print(json.dumps(french_text, indent=2, ensure_ascii=False))

    return french_text.get("translations")[0].get("translation")


def french_to_english(french_text):
    '''function to tranlate french to english'''

    english_text = LANGUAGE_TRANSLATOR.translate(text=french_text, model_id='fr-en').get_result()
    #print(json.dumps(english_text, indent=2, ensure_ascii=False))
    return english_text.get("translations")[0].get("translation")
