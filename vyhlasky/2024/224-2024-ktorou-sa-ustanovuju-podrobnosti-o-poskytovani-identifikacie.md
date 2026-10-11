---
title: "Vyhláška Ministerstva vnútra Slovenskej republiky, ktorou sa ustanovujú podrobnosti o poskytovaní identifikácie volajúceho a o poskytovaní lokalizačných údajov"
identifier: "224/2024 Z. z."
eli: "https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/2024/224/"
type: decree
jurisdiction: sk
language: sk
date: 2024-08-28
last_amended: 2024-09-01
status: in_force
consolidated_version: "/SK/ZZ/2024/224/20240901"
source: "https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/2024/224/20240901"
retrieved: 2026-10-12
---

# Vyhláška Ministerstva vnútra Slovenskej republiky, ktorou sa ustanovujú podrobnosti o poskytovaní identifikácie volajúceho a o poskytovaní lokalizačných údajov

**224**

**VYHLÁŠKA**

**Ministerstva vnútra Slovenskej republiky**

**z 15. augusta 2024,**

**ktorou sa ustanovujú podrobnosti o poskytovaní identifikácie volajúceho a o poskytovaní lokalizačných údajov**

Ministerstvo vnútra Slovenskej republiky (ďalej len „ministerstvo“) podľa § 111 ods. 10 zákona č. 452/2021 Z. z. o elektronických komunikáciách (ďalej len „zákon“) po dohode s Ministerstvom dopravy Slovenskej republiky ustanovuje:

## § 1

(1) Tiesňovou komunikáciou na účely tejto vyhlášky sa rozumie

a) tiesňové volanie na čísla tiesňového volania určené národným číslovacím plánom<sup>1</sup>) uskutočnené prostredníctvom verejne dostupnej interpersonálnej komunikačnej služby založenej na číslach,

b) tiesňové volanie z verejnej mobilnej siete, pri ktorom číslo volajúceho nie je k dispozícii,

c) SMS<sup>2</sup>) zaslaná na jednotné európske číslo tiesňového volania „112“,

d) tiesňové volanie koncového užívateľa, zákazníka cudzozemského poskytovateľa verejne dostupných mobilných interpersonálnych komunikačných služieb založených na číslach, prihláseného do siete podniku poskytujúceho verejnú mobilnú sieť na základe veľkoobchodnej zmluvy o prístupe k roamingu,

e) verejne dostupná interpersonálna komunikačná služba založená na číslach poskytovaná prostredníctvom pevnej siete, ktorá nie je viazaná na konkrétny koncový bod pevnej siete, alebo verejná dostupná interpersonálna komunikačná služba založená na číslach poskytovaná v pevnom umiestnení, ku ktorej možno pristupovať z ktoréhokoľvek miesta v oblasti pokrytia bez možnosti využívania služby počas presunu koncového zariadenia užívateľa.

(2) Identifikáciou volajúceho alebo identifikáciou odosielateľa SMS sa rozumie poskytnutie jeho telefónneho čísla,<sup>3</sup>) poskytnutie identifikácie účastníka podľa § 111 ods. 8 písm. b) zákona a identifikácia siete podniku, v ktorej tiesňové volanie vzniklo, podľa § 2 ods. 5.

## § 2

(1) Telefónne číslo volajúceho sa poskytuje v tvare podľa prílohy časti A. Pri tiesňovom volaní podľa § 1 ods. 1 písm. b) sa namiesto telefónneho čísla volajúceho poskytuje medzinárodné označenie mobilného koncového zariadenia (IMEI).<sup>4</sup>)

(2) Telefónne číslo volajúceho a IMEI sa na rozhraní medzi podnikom a koordinačným strediskom integrovaného záchranného systému alebo operačným strediskom tiesňového volania (ďalej len „stredisko“) prenášajú

a) pri použití ISDN užívateľskej časti (ISUP)<sup>5</sup>) signalizačného systému SS7 v parametri Calling Party Number<sup>6</sup>) signalizačnej správy Initial Address Message (IAM),<sup>7</sup>)

b) pri použití signalizačného protokolu SIP v záhlaví P-Asserted-Identity signalizačnej správy INVITE vo forme SIP URI a v záhlaví Contact vo forme URN.

(3) Identifikačné údaje účastníka podľa § 111 ods. 8 písm. b) zákona sa poskytujú prostredníctvom protokolu Simple Object Access Protocol (SOAP) prostredníctvom webovej služby Web Services Description Language (WSDL) zverejnenej na webovom sídle ministerstva do 15 sekúnd od vyžiadania strediskom.

(4) Pri tiesňovom volaní podľa § 1 ods. 1 písm. b) a d) a pri volaní eCall<sup>8</sup>) sa identifikačné údaje účastníka podľa § 111 ods. 8 písm. b) zákona neposkytujú.

(5) Na identifikáciu siete, v ktorej tiesňové volanie vzniklo, sa používa sieťové smerovacie číslo v tvare podľa osobitného predpisu.<sup>9</sup>)

(6) Na prenos sieťového smerovacieho čísla podľa odseku 5 sa využíva

a) pri použití ISDN užívateľskej časti (ISUP) signalizačného systému SS7 parameter Called Party Number<sup>10</sup>) signalizačnej správy IAM,

b) pri použití signalizačného protokolu SIP v záhlaví P-Access-Network-Info parameter operator-specific-GI v signalizačnej správe INVITE.

(7) Na identifikáciu odosielateľa SMS podľa § 1 ods. 1 písm. c) sa obdobne použijú odseky 1 a 3, ak SMS podľa § 1 ods. 1 písm. c) je

a) zo siete podniku do strediska prenášaná prostredníctvom protokolu Short Message Peer-to-Peer Protocol (SMPP),

b) možné odoslať len z registrovaného koncového zariadenia, preto telefónne číslo odosielateľa SMS podľa § 1 ods. 1 písm. c) sa vždy použije.

## § 3

(1) Pri tiesňovom volaní z pevnej siete minimálnym rozsahom lokalizačných údajov je adresa umiestnenia koncového bodu siete určená v zmluve o poskytovaní služieb.

(2) Ak sa tiesňové volanie uskutočňuje z pevnej siete podľa § 1 ods. 1 písm. e), poskytne sa o tom informácia spolu s lokalizačnými údajmi podľa odseku 1, ak ich má podnik k dispozícii.

(3) Údaje podľa odsekov 1 a 2 sa poskytujú prostredníctvom protokolu SOAP prostredníctvom webovej služby WSDL.

## § 4

(1) Pri tiesňovom volaní z mobilnej siete minimálnym rozsahom lokalizačných údajov sú

a) identifikátor sektora základňovej stanice (označenie bunky) siete, v ktorej tiesňové volanie vzniklo,

b) údaje potrebné na geografické znázornenie identifikovaného sektora základňovej stanice (označenie bunky) na mapovom podklade.

(2) Identifikátor sektora základňovej stanice podľa odseku 1 písm. a) sa poskytuje v tvare podľa prílohy časti B.

(3) Údaj podľa odseku 1 písm. a) sa poskytuje

a) pri použití ISDN užívateľskej časti (ISUP) signalizačného systému SS7 v parametri Location Number<sup>11</sup>) signalizačnej správy IAM,

b) pri použití signalizačného protokolu SIP v záhlaví P-Access-Network-Info signalizačnej správy INVITE.

(4) Údaje podľa odseku 1 písm. b) sa poskytujú z protokolu Mobile Location Protocol (MLP verzia 3.2) alebo Mobile Location Protocol (MLP verzia 3.5) na základe telefónneho čísla volajúceho alebo medzinárodného označenia mobilného účastníka (IMSI),<sup>12</sup>) pri tiesňovom volaní podľa § 1 ods. 1 písm. b) na základe čísla bunky.

(5) Ak lokalizačný údaj podľa odseku 1 nemožno pri poskytovaní siete a služby počas trvania tiesňového volania získať alebo ide o tiesňové volanie podľa § 1 ods. 1 písm. e), namiesto údaja podľa odseku 1 písm. a) sa v poli označenie bunky poskytuje reťazec v tvare sieťové smerovacie číslo a dohodnutý číselný reťazec; údaje podľa odseku 1 písm. b) sa neposkytujú.

(6) Pri odoslaní SMS podľa § 1 ods. 1 písm. c) účastníkom minimálnym rozsahom lokalizačných údajov sú údaje podľa odseku 1 písm. b).

## § 5

(1) Lokalizačné údaje podľa § 4 ods. 1 písm. a) sa poskytujú v okamihu zostavenia tiesňovej komunikácie. Lokalizačné údaje podľa § 4 ods. 1 písm. b) sa poskytujú do 15 sekúnd od okamihu zostavenia tiesňovej komunikácie a ich vyžiadania strediskom.

(2) Lokalizačné údaje podľa § 4 ods. 1 písm. b) sa poskytujú aj na základe ich opätovného vyžiadania strediskom, ak možno lokalizačné údaje v čase opätovného vyžiadania zistiť, najviac však do 48 hodín od uskutočnenia tiesňovej komunikácie. Pri opätovnom vyžiadaní sa lokalizačné údaje poskytujú do 30 sekúnd od ich opätovného vyžiadania.

(3) Údaje, ktoré označujú polohu koncového zariadenia účastníka, získané prostredníctvom funkcionality koncového zariadenia sa prenášajú sieťou podniku do strediska, a to bez zmien, bezodkladne po ich prijatí sieťou podniku z koncového zariadenia.

## § 6

(1) Pri zostavovaní tiesňového volania sa používa formát telefónneho čísla volaného ustanovený v prílohe časti C.

(2) Tiesňové volania sa zo siete podniku, ktorý nie je poskytovateľom verejnej mobilnej siete, smerujú priamo alebo nepriamo do siete poskytovateľa verejnej mobilnej siete. Údaje podľa tejto vyhlášky týkajúce sa volaní, ktoré vznikli v sieti iného podniku, sa pri prenose tiesňového volania vlastnou sieťou podniku prenášajú bez zmien.

(3) Smerovanie tiesňových volaní v mobilnej sieti na príslušné stredisko sa zabezpečuje na základe lokalizačných údajov v čase zostavovania tiesňového volania a na základe signalizácie koncového zariadenia podľa prílohy časti D. Tiesňové volanie podľa § 1 ods. 1 písm. e) sa smeruje na stredisko určené ministerstvom.

(4) Údaje podľa tejto vyhlášky sa prenášajú od podniku poskytujúceho verejne dostupnú interpersonálnu komunikačnú službu založenú na číslach, v ktorého sieti tiesňová komunikácia vznikla.

## § 7

Táto vyhláška nadobúda účinnosť 1. septembra 2024.

v z. Patrik Krauspe v. r.

## Prílohy

### Príloha k vyhláške č. 224/2024 Z. z.

**TVAR POSKYTOVANÝCH IDENTIFIKAČNÝCH ÚDAJOV A LOKALIZAČNÝCH ÚDAJOV**

**ČASŤ A — Tvar telefónneho čísla volajúceho a medzinárodné označenie mobilného koncového zariadenia**

1. Tvar telefónneho čísla volajúceho pri národnom volaní

SS7/ISUP parameter Calling Party Number

Address signals = národný cieľový kód (NDC) + účastnícke číslo (SN)

Nature of Address indicator = national (significant) number

Screening indicator = user provided, verified and passed / network provided

alebo

Address signals = kód krajiny (CC = 421) + národný cieľový kód (NDC) + účastnícke číslo (SN)

Nature of Address indicator = international number

Screening indicator = user provided, verified and passed / network provided

2. Tvar telefónneho čísla volajúceho pri tiesňovom volaní podľa § 1 ods. 1 písm. d)

SS7/ISUP parameter Calling Party Number

Address signals = kód krajiny (CC) + národný cieľový kód (NDC) + účastnícke číslo (SN)

Nature of Address indicator = international number

Screening indicator = user provided, verified and passed / network provided

3. Medzinárodné označenie volajúceho pri tiesňovom volaní podľa § 1 ods. 1 písm. b)

SS7/ISUP parameter Calling Party Number

Address signals = IMEI

Nature of Address indicator = national (significant) number / unknown / international number

Screening indicator = user provided, not verified

Číslice IMEI sa prenášajú ako binárne kódované dekadické číslice v poradí pridelený kód typu (TAC), sériové číslo (SNR), rezervná číslica (SD). Číslica kódu TAC s najvyššou váhou sa prenáša v 4-bitovom poli na pozícii 1<sup>st</sup> address signal. Nasledujúce číslice sa prenášajú postupne v po sebe idúcich 4-bitových poliach. Rezervná číslica SD sa prenáša na pozícii 15<sup>th</sup> address signal, pozícia

16<sup>th</sup>address signal obsahuje výplň.<sup>13</sup>)

**ČASŤ B — Tvar identifikátora sektora základňovej stanice**

1. Mobilné siete druhej generácie a tretej generácie

Ako identifikátor sektora základňovej stanice sa používa Cell Global Identification (CGI),<sup>14</sup>) ktorý sa skladá z týchto častí:

a) Mobilný kód krajiny (MCC) identifikuje krajinu, v ktorej sa nachádza verejná pozemná mobilná sieť (PLMN). Mobilný kód krajiny pridelený Slovenskej republike je 231.

b) Kód mobilnej siete (MNC) je kód identifikujúci verejnú pozemnú mobilnú sieť (PLMN) v danej krajine. V Slovenskej republike je kód mobilnej siete dvojmiestny.

c) Kód lokalizačnej oblasti (LAC) je kód pevnej dĺžky (2 oktety) identifikujúci lokalizačnú oblasť v rámci verejnej pozemnej mobilnej siete (PLMN). Na vyjadrenie úplného rozsahu hodnôt uvedeného parametra v dekadickom formáte je potrebných 5 dekadických číslic.

d) Identita bunky (CI) je kód pevnej dĺžky (2 oktety) identifikujúci bunku v rámci lokalizačnej oblasti. Identita bunky musí byť jedinečná v rámci lokalizačnej oblasti. Na vyjadrenie úplného rozsahu hodnôt uvedeného parametra v dekadickom formáte je potrebných 5 dekadických číslic.

Dĺžka CGI je 15 dekadických číslic. Ak ide o prenos CGI podľa § 4 ods. 3 písm. a) sa jeho hodnoty prenášajú v dekadickom formáte.

2. Mobilné siete štvrtej generácie a piatej generácie

Ako identifikátor sektora základňovej stanice sa používa E-UTRAN Cell Global Identification (ECGI),<sup>15</sup>) ktorý je vytvorený spojením

a) identifikátora verejnej pozemnej mobilnej siete PLMN (PLMN-Id) tvoreného mobilným kódom krajiny (MCC) a kódom mobilnej siete (MNC) a

b) identity bunky E-UTRAN (ECI), ktorá má pevnú dĺžku 28 bitov. ECI pozostáva z dvoch častí: eNodeB ID a Physical Cell ID. eNodeB ID predstavuje jedinečné identifikačné číslo pridelené každej eNodeB (základňovej stanici) v sieti. Physical Cell ID označuje identifikátor fyzickej vrstvy konkrétnej bunky v rámci eNodeB. Na vyjadrenie úplného rozsahu hodnôt ECI v dekadickom formáte je potrebných 9 dekadických číslic.

Keďže kód mobilnej siete (MNC) v Slovenskej republike je dvojmiestne číslo, dĺžka ECGI je 14 dekadických číslic. V prípade prenosu ECGI podľa § 4 ods. 3 písm. a) sa jeho hodnoty prenášajú v dekadickom formáte.

**ČASŤ C — Formát telefónneho čísla volaného**

1. Volania na čísla tiesňových volaní 112 a 155

SS7/ISUP parameter Called Party Number

Address signals = národný cieľový kód (NDC) + číslo tiesňového volania + sieťové smerovacie číslo (NRN)

Nature of Address indicator = national (significant) number

2. Volania na čísla tiesňových volaní 150 a 158

SS7/ISUP parameter Called Party Number

Address signals = národný cieľový kód (NDC) + číslo tiesňového volania + číslo atrakčného obvodu v tvare XY podľa zoznamu určeného ministerstvom a zverejneného na webovom sídle ministerstva + sieťové smerovacie číslo (NRN)

Nature of Address indicator = national (significant) number

**ČASŤ D — Pravidlá smerovania tiesňových volaní na základe signalizácie koncového zariadenia mobilnej siete**

1. Mobilné siete druhej generácie a tretej generácie

Na základe obsahu oktetu 3 informačného elementu Service Category generovaného koncovým zariadením mobilnej siete v rámci protokolu CC (Call Control)<sup>16</sup>) sa tiesňové volania smerujú takto:

<table>
<tr>
<td colspan="2">**Oktet 3 informačného elementu Service Category – Emergency Service Category Value**</td>
</tr>
<tr>
<td>**Hodnota bitov**</td>
<td>**Smerovanie**</td>
</tr>
<tr>
<td>Bit 1 (Police) = 1, ostatné bity = 0</td>
<td>NDC+158+číslo atrakčného obvodu+NRN</td>
</tr>
<tr>
<td>Bit 2 (Ambulance) = 1, ostatné bity = 0</td>
<td>NDC+155+NRN​</td>
</tr>
<tr>
<td>Bit 3 (Fire Brigade) = 1, ostatné bity = 0</td>
<td>NDC+150+číslo atrakčného obvodu+NRN</td>
</tr>
<tr>
<td>Bit 4 (Marine Guard) = 1, ostatné bity = 0</td>
<td>NDC+112+NRN</td>
</tr>
<tr>
<td>Bit 5 (Mountain Rescue) = 1, ostatné bity = 0</td>
<td>NDC+112+NRN</td>
</tr>
<tr>
<td>Bit 6 (Manually Initiated eCall) = 1, ostatné bity = 0</td>
<td>NDC+11202+NRN</td>
</tr>
<tr>
<td>Bit 7 (Automatically Initiated eCall) = 1, ostatné bity = 0</td>
<td>NDC+11201+NRN</td>
</tr>
<tr>
<td>Bit 8 (Spare) = 1, ostatné bity = 0</td>
<td>NDC+112+NRN</td>
</tr>
<tr>
<td>Všetky bity nastavené na hodnotu 0</td>
<td>NDC+112+NRN</td>
</tr>
<tr>
<td>Dva a viac bitov nastavených na hodnotu 1, vrátane situácie, keď sú naraz nastavené bity 6 aj 7 na hodnotu 1</td>
<td>NDC+112+NRN</td>
</tr>
</table>

2. Mobilné siete štvrtej generácie a piatej generácie

Na základe obsahu Request-URI prenášaného v počiatočnom riadku signalizačnej správy INVITE signalizačného protokolu SIP generovaného koncovým zariadením mobilnej siete<sup>17</sup>) sa tiesňové volania smerujú takto:

<table>
<tr>
<td colspan="2">**Request-URI obsahujúci identitu tiesňovej služby**</td>
</tr>
<tr>
<td>**Jednotný názov zdroja (URN)**</td>
<td>**Smerovanie**</td>
</tr>
<tr>
<td>urn:service:sos</td>
<td>NDC+112+NRN</td>
</tr>
<tr>
<td>urn:service:sos.fire</td>
<td>NDC+150+číslo atrakčného obvodu+NRN</td>
</tr>
<tr>
<td>urn:service:sos.ambulance</td>
<td>NDC+155+NRN</td>
</tr>
<tr>
<td>urn:service:sos.police</td>
<td>NDC+158+číslo atrakčného obvodu+NRN</td>
</tr>
<tr>
<td>urn:service:sos.* <br> (* znamená akýkoľvek iný reťazec, vrátane marine a mountain)</td>
<td>NDC+112+NRN</td>
</tr>
</table>

## Poznámky pod čiarou

1) § 18 ods. 6 vyhlášky Úradu pre reguláciu elektronických komunikácií a poštových služieb č. 286/2022 Z. z. o národnom číslovacom pláne.

2) ETSI TS 123 040 (3GPP TS 23.040): Technical realization of the Short Message Service (SMS).

3) ITU-T Recommendation E.164: The international public telecommunication numbering plan.

4) ETSI TS 123 003 (3GPP TS 23.003): Numbering, addressing and identification, kapitola 6.2.1.

5) ITU-T Recommendation Q.761: Signalling System No. 7 – ISDN user part functional description.

6) ITU-T Recommendation Q.763: Signalling System No. 7 – ISDN user part formats and codes, kapitola 3.10.

7) ITU-T Recommendation Q.763: Signalling System No. 7 – ISDN user part formats and codes, kapitola 4, tabuľka 32/Q.763.

8) Čl. 3 ods. 2 nariadenia Európskeho parlamentu a Rady (EÚ) 2015/758 z 29. apríla 2015 o požiadavkách typového schválenia pri zavádzaní palubného systému eCall využívajúceho službu tiesňovej linky 112 a o zmene smernice 2007/46/ES (Ú. v. EÚ L 123, 19. 5. 2015) v platnom znení.

9) § 15 vyhlášky č. 286/2022 Z. z.

10) ITU-T Recommendation Q.763: Signalling System No. 7 – ISDN user part formats and codes, kapitola 3.9.

11) ITU-T Recommendation Q.763: Signalling System No. 7 – ISDN user part formats and codes, kapitola 3.30.

12) ETSI TS 123 003 (3GPP TS 23.003): Numbering, addressing and identification, kapitola 2.2.

13) ITU-T Recommendation Q.763: Signalling System No. 7 – ISDN user part formats and codes, kapitola 3.9 písm. f).

14) ETSI TS 123 003 (3GPP TS 23.003): Numbering, addressing and identification, kapitola 4.3.1.

15) ETSI TS 123 003 (3GPP TS 23.003): Numbering, addressing and identification, kapitola 19.6.

16) ETSI TS 124 008 (3GPP TS 24.008): Mobile radio interface Layer 3 specification; Core network protocols; Stage 3, kapitola 10.5.4.33.

17) ETSI TS 124 229 (3GPP TS 24.229): IP multimedia call control protocol based on Session Initiation Protocol (SIP) and Session Description Protocol (SDP); Stage 3, kapitola 5.1.6.8, IETF RFC 5031: A Uniform Resource Name (URN) for Emergency and Other Well-Known Services.
