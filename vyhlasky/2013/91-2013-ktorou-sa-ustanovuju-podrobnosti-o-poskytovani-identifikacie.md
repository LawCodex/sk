---
title: "Vyhláška Ministerstva vnútra Slovenskej republiky, ktorou sa ustanovujú podrobnosti o poskytovaní identifikácie volajúceho a o poskytovaní lokalizačných údajov"
identifier: "91/2013 Z. z."
eli: "https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/2013/91/"
type: decree
jurisdiction: sk
language: sk
date: 2013-04-19
last_amended: 2013-07-01
status: in_force
consolidated_version: "/SK/ZZ/2013/91/20130701"
source: "https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/2013/91/20130701"
retrieved: 2026-10-12
---

# Vyhláška Ministerstva vnútra Slovenskej republiky, ktorou sa ustanovujú podrobnosti o poskytovaní identifikácie volajúceho a o poskytovaní lokalizačných údajov

**91**

**VYHLÁŠKA**

**Ministerstva vnútra Slovenskej republiky**

**z 10. apríla 2013,**

**ktorou sa ustanovujú podrobnosti o poskytovaní identifikácie volajúceho a o poskytovaní lokalizačných údajov**

Ministerstvo vnútra Slovenskej republiky (ďalej len „ministerstvo“) podľa § 57 ods. 13 zákona č. 351/2011 Z. z. o elektronických komunikáciách po dohode s Ministerstvom dopravy, výstavby a regionálneho rozvoja Slovenskej republiky ustanovuje:

## § 1

Táto vyhláška ustanovuje podrobnosti o poskytovaní identifikácie volajúceho a o poskytovaní lokalizačných údajov pri tiesňovom volaní na koordinačné stredisko integrovaného záchranného systému alebo na operačné stredisko tiesňového volania (ďalej len „stredisko“).

## § 2

Na účely tejto vyhlášky sa tiesňovým volaním rozumie volanie z verejnej elektronickej komunikačnej siete (ďalej len „sieť“) na číslo tiesňového volania podľa osobitného predpisu.<sup>1</sup>)

## § 3

(1) Telefónne číslo volajúceho a medzinárodné označenie mobilného koncového zariadenia (IMEI) v parametri Calling Party Number signalizačnej správy SETUP protokolu Digital Subscriber Signaling System Nr.1 (DSS - 1) alebo v signalizačnej správe Initial Address Message (IAM) signalizačného protokolu Signaling System 7 - ISDN User Part (SS7 - ISUP) sa poskytujú v tvare podľa prílohy.

(2) Na identifikáciu volajúceho sa poskytujú údaje prostredníctvom protokolu Simple Object Access Protocol (SOAP) prostredníctvom webovej služby Web Services Description Language (WSDL) zverejnenej na webovom sídle ministerstva do 15 sekúnd od vyžiadania strediskom pri dostupnosti identifikácie volajúceho 98 %; údaje možno vyžiadať do 48 hodín od tiesňového volania.

(3) Na identifikáciu siete, v ktorej tiesňové volanie vzniklo, využíva sa parameter Called Party Number signalizačnej správy SETUP protokolu Digital Subscriber Signaling System Nr.1 (DSS - 1) alebo signalizačnej správy Initial Address Message (IAM) signalizačného protokolu Signaling System 7 - ISDN User Part (SS7 - ISUP).

## § 4

(1) Lokalizačné údaje sa poskytujú do 15 sekúnd od prijatia tiesňového volania a od ich vyžiadania strediskom pri dostupnosti poskytovania lokalizačných údajov 99,5 %.

(2) Lokalizačné údaje sa poskytujú aj na základe opätovného vyžiadania strediskom, ak možno lokalizačné údaje v čase opätovného vyžiadania zistiť, najviac však do 48 hodín od uskutočnenia tiesňového volania; lokalizačné údaje sa poskytujú do 30 sekúnd od ich vyžiadania pri dostupnosti poskytovania lokalizačných údajov 99,5 %.

## § 5

(1) Pri tiesňovom volaní z pevnej siete minimálnym rozsahom lokalizačných údajov je adresa koncového bodu siete.

(2) Údaje podľa odseku 1 sa poskytujú prostredníctvom protokolu Simple Object Access Protocol (SOAP) prostredníctvom webovej služby Web Services Description Language (WSDL) zverejnenej na webovom sídle ministerstva.

## § 6

(1) Pri tiesňovom volaní z mobilnej siete minimálnym rozsahom lokalizačných údajov sú:

a) identifikátor sektora základňovej stanice (označenie bunky),

b) geografické znázornenie identifikovaného sektora základňovej stanice (označenie bunky).

(2) Údaje podľa odseku 1 písm. a) sa poskytujú v signalizačnom parametri Location Number signalizačnej správy Initial Address Message (IAM) signalizačného protokolu Signaling System 7 - ISDN User Part (SS7 - ISUP). Identifikátor sektora základňovej stanice (označenie bunky), v ktorej tiesňové volanie vzniklo, poskytuje sa v tvare podľa prílohy.

(3) Údaje podľa odseku 1 písm. b) sa poskytujú prostredníctvom protokolu Mobile Location Protocol (MLP). Na poskytovanie lokalizačných údajov volajúceho sa používa telefónne číslo volajúceho alebo identifikátor sektora základňovej stanice (označenie bunky).

## § 7

(1) Stredisko vyžaduje údaje podľa tejto vyhlášky od podniku poskytujúceho verejnú elektronickú komunikačnú službu, v ktorého sieti tiesňové volanie vzniklo.

(2) Údaje podľa tejto vyhlášky sa poskytujú stredisku prostredníctvom ministerstva.

## § 8

Zrušuje sa vyhláška Ministerstva vnútra Slovenskej republiky č. 612/2008 Z. z. o podrobnostiach poskytovania zobrazovania identifikácie volajúcej stanice a poskytovania lokalizačných údajov koordinačnému stredisku alebo operačnému stredisku integrovaného záchranného systému.

## § 9

Táto vyhláška nadobúda účinnosť 1. júla 2013.

Robert Kaliňák v. r.

## Prílohy

### Príloha k vyhláške č. 91/2013 Z. z. — TVAR POSKYTOVANÝCH IDENTIFIKAČNÝCH A LOKALIZAČNÝCH ÚDAJOV

**ČASŤ A. Telefónne číslo volajúceho a medzinárodné označenie mobilného koncového zariadenia**

**Parametre Calling Party Number a Nature of Address Indicator**

a) Telefónne číslo volajúceho pri národnom volaní:

Calling Party Number = Národný cieľový kód (NDC) + účastnícke číslo (SN)

Nature of Address Indicator = National

alebo

Calling Party Number = Medzinárodné smerové číslo (CC = 421) + Národný cieľový kód (NDC) + účastnícke číslo (SN)

Nature of Address Indicator = International.

b) Telefónne číslo volajúceho v prípade medzinárodného účastníka v roamingu:

Calling Party Number = Medzinárodné smerové číslo (CC) + Národný cieľový kód (NDC) + účastnícke číslo (SN)

Nature of Address Indicator = International.

c) Medzinárodné označenie koncového zariadenia

Calling Party Number = IMEI

Nature of Address Indicator = National/Unknown/International.

**ČASŤ B. Telefónne číslo volaného**

**Parametre Called Party Number a Nature of Address Indicator,**

a) ak ide o volania na čísla tiesňových volaní 112 a 155:

Called Party Number = Národný cieľový kód (NDC) + číslo tiesňového volania + sieťové smerovacie číslo (NRN)

Nature of Address Indicator = National,

b) ak ide o volania na čísla tiesňových volaní 150 a 158:

Called Party Number = Národný cieľový kód (NDC) + číslo tiesňového volania + číslo atrakčného obvodu + sieťové smerovacie číslo (NRN)

Nature of Address Indicator = National.

Poznámky:

Národný cieľový kód (NDC) = identifikátor operačného strediska v tvare národného cieľového kódu primárnej oblasti, kde má byť volanie odovzdané do strediska,

sieťové smerovacie číslo (NRN) = identifikátor siete podniku, v ktorej tiesňové volanie vzniklo, v tvare podľa § 21 opatrenia z 8. decembra 2011 č. O-26/2011 (oznámenie č. 466/2011 Z. z.),

číslo atrakčného obvodu = identifikátor atrakčného obvodu v tvare xy podľa zoznamu zverejneného na webovom sídle ministerstva.

**ČASŤ C. Location number**

**Cell Global Identification (CGI) = Mobile Country Code (MCC) + Mobile Network Code (MNC) + Location Area Code (LAC) + Cell Identity (CI).**

Podľa technickej špecifikácie ETSI TS 123 003.

Location Number má jednotnú dĺžku 15 číslic.

## Poznámky pod čiarou

1) Opatrenie Telekomunikačného úradu Slovenskej republiky z 8. decembra 2011 č. O-26/2011 o číslovacom pláne (oznámenie č. 466/2011 Z. z.).
