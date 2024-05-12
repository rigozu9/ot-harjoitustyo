# Science based daily planner

Tieteelliseen tietoon perustuva päivittäinen suunnitteluohjelma parempien päivittäisten tapojen kehittämiseen. 
Käyttäjät voivat rekisteröityä ja kirjautua sisään. Ensikertalaisille on kysely. 
Kyselyssä asetetaan tavoitteita ja kerrotaan perustietoja.
Kalenteria selatessa voi tarkastella eri päivien aktiviteetteja. 
Profiilinäkymästä voi tarkastella omia tavoitteita ja aktiviteettien keskiarvoja. 
Lisäksi voit verrata keskiarvojasi asettamiisi tavoitteisiin. 
Käyttäjä saa omiin tietoihin räätälöityjä parannusehdotuksia ja linkkejä mistä voi lukea enemmän infoa.
Kun syötät päivän aktiviteetit, saat vertailutietoja tavoitteisiisi nähden.

### Dokumentaatio

[Vaatimusmäärittely](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/dokumentaatio/arkkitehtuuri.md)

[Testaus](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/dokumentaatio/testaus.md)

[Releases](https://github.com/rigozu9/ot-harjoitustyo/releases)


## Nopea asennus

### (Tarkemmat ohjeet löytyvät täältä):
[Käyttöohje](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/dokumentaatio/kayttoohje.md)

1. Kloona projekti ssh komennolla: 
```bash
git clone git@github.com:rigozu9/ot-harjoitustyo.git
```
tai https:
```bash
git clone https://github.com/rigozu9/ot-harjoitustyo.git
```
- TAI
1. Lataa loppupalautus release [täältä](https://github.com/rigozu9/ot-harjoitustyo/releases)

2. Navigoi daily-planner-app folderiin ja asenna riippuvuudet komennolla:

```bash
poetry install
```

### Ohjelman suorittaminen
Mene poetryn virtual enviin komennolla: 

```bash
poetry shell
```

Ja suorita ohjelma komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint tarkistus

Pylintin tarkistus komento:

```bash
poetry run invoke lint
```
