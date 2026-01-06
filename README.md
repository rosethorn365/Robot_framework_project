
# Invoice Processing with Robot Framework & MySQL

End-to-end automaatio, joka lukee laskujen header- ja riviaineiston CSV:istä, validoi datan (viitenumero, IBAN, rivisummat) ja kirjoittaa tuloksen MySQL-tietokantaan statuksineen.

## Ominaisuudet
- Parsii `InvoiceHeaderData.csv` ja `InvoiceRowData.csv` (`;` erotin)
- Validointi: **Suomalainen viitenumero**, **IBAN (ISO 13616)**, **header vs. rivisummat**
- Tallennus tauluihin `invoiceheader` ja `invoicerow` + **status**: OK / Reference number error / IBAN number error / Amount difference

## Esivaatimukset
- Python 3.10+
- MySQL 8.x
- Robot Framework & PyMySQL
```bash
pip install robotframework robotframework-databaselibrary pymysql
