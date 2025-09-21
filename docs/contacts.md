# Contacts
The Contacts service provides access to contacts via a RESTful API interface.

## Contacts data pipeline
The source contact data is hosted by user Apple iCloud account, which syncs to their mobile iOS device contacts.

__01 iCloud VCF file export__
Data is imported into the service via manual user export from logging into iCloud and exporting contacts as `*.vcf` file.

__02 VCF file upload OneDrive__
The user manually uploads the VCF file to OneDrive cloud storage.

__03 VCF file ingest to Blob stoage__
An automation workflow such as Logic App periodically ingests the VCF file to Blob storage

__04 App read VCF file__
The API app reads the contacts from the VCF and makes them available to the user via RESTful interface.

## VCF parsing to JSON

__VCARD format__

The *.vcf file format is a collection of contact cards in VCARD format in plain UTF-8 text.  Each VCARD is delimited by beginning market `BEGIN:VCARD` and end marker `END:VCARD`

```
BEGIN:VCARD
VERSION:3.0
PRODID:-//Apple Inc.//iOS 5.0.1//EN
N:A.;Gilberto;;;
FN:Gilberto A.
item1.EMAIL;type=INTERNET;type=pref:Gilberto.Andujar@avlhq.com
item1.X-ABLabel:_$!<Other>!$_
TEL;type=CELL;type=VOICE;type=pref:9549743903
REV:2012-07-20T04:45:28Z
END:VCARD
```

__attributes__
Contact attributes can be extracted from the card using simple regex patterns

| attribute | regex |
| - | - |
| name | `^FN:(.*?)$` |
| phone | `^TEL.*:(.*?)$` |
