#!/usr/bin/env python3
"""parses user contacts file from *.vcf to JSON format
"""
# dependencies ---------------------------------------------------------
import os
import sys
import json
import re


# constants ---------------------------------------------------------
CONTACTS_JSON_FILE = 'contacts.json'
VCARD_PATTERN = r'BEGIN:VCARD(.*?)END:VCARD'
NAME_PATTERN = r'^FN:(.*?)$'
PHONE_PATTERN = r'^TEL.*:(.*?)$'


# functions ---------------------------------------------------------
def parse_vcf_card(card_str):
    card = {}
    name_matches = re.search(NAME_PATTERN, card_str, re.MULTILINE)
    phone_matches = re.search(PHONE_PATTERN, card_str, re.MULTILINE)
    if name_matches:
        card['name'] = name_matches.group(1)
    if phone_matches:
        card['phone'] = phone_matches.group(1)
    return card


def get_vcf_cards(vcf_str):
    cards = re.findall(VCARD_PATTERN, vcf_str, re.DOTALL)
    if not cards:
        raise ValueError(f'ERROR. no cards found')
    return cards


def parse_cards_to_dict(vcf_cards):
    cards = []
    for c in vcf_cards:
        card = parse_vcf_card(c)
        if card:
            cards.append(card)
    return cards


def parse_vcf(vcf_file):
    vcf_cards_str = ''
    try:
        with open(vcf_file, 'r', encoding='utf-8') as f:
            vcf_cards_str = f.read()
            f.close()
    except Exception as e:
        raise IOError(f'problem opening VCF file {vcf_file}') from e

    try:
        vcf_cards = get_vcf_cards(vcf_cards_str)
        cards = parse_cards_to_dict(vcf_cards)
    except Exception as e:
        raise ValueError(f'problem parsing VCF cards.') from e

    # export to JSON file
    try:
        with open(CONTACTS_JSON_FILE, 'w') as f:
            json.dump(cards, f, indent=3)
            f.close()
    except Exception as e:
        raise IOError(f'problem writing to JSON file {CONTACTS_JSON_FILE}') from e

    #print(f'SUCCESS. read {len(vcf_cards_str)} char from VCF card file. \n VCF cards file preview: \n {vcf_cards_str[:500]}')
    #print(f'SUCCESS. found {len(cards)} VCF cards. \n first 10x card \n {cards[:9]}')
    print(f'SUCCESS. parsed iCloud VCF contacts and saved to JSON file {CONTACTS_JSON_FILE}.')

# entry point ---------------------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) > 1:
        vcf_file = sys.argv[1]
        if os.path.exists(vcf_file):
            parse_vcf(vcf_file)
        else:
            raise ValueError(f"file {vcf_file} does not exist")
    else:
        raise ValueError("missing positional argument <vcf_file>")
