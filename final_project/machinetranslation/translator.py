"""Watson Translator module translating Eglish to French and vice versa"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(en_text: str):
    """English To French"""
    translation = language_translator.translate(
        text=en_text,
        model_id='en-fr').get_result()
    en_text = translation['translations'][0]['translation']
    return en_text

def french_to_english(fr_text: str):
    """French to English"""
    translation = language_translator.translate(
        text=fr_text,
        model_id='fr-en').get_result()
    fr_text = translation['translations'][0]['translation']
    return fr_text
