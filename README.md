# Science based daily planner

A sciene based daily planner program to help develop better daily habits. 
User can be registered and logged in.
Survey for first time users.
Can add and delete activites.

Testattu koulun fuksiläppärillä ja toimi oikein.

### Dokumentaatio

[Vaatimusmäärittely](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/dokumentaatio/arkkitehtuuri.md)


## Asennus

1. Kloona projekti ssh komennolla: 
```bash
git clone git@github.com:rigozu9/ot-harjoitustyo.git
```
tai https:
```bash
git clone https://github.com/rigozu9/ot-harjoitustyo.git
```
2. Navigoi daily-planner-app folderiin ja asenna riippuvuudet komennolla:

```bash
poetry install
```

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

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