# Science based daily plannmer

A sciene based daily planner program to help develop better daily habits.

### Dokumentaatio
[Vaatimusmäärittely](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/dokumentaatio/vaatimusmaarittely.md)
[Tuntikirjanpito](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/dokumentaatio/tuntikirjanpito.md)  
[Changelog](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/dokumentaatio/changelog.md) 

## Asennus

1. Kloona projekti ssh komennolla: 
```bash
git clone git@github.com:rigozu9/ot-harjoitustyo.git
```
tai https:
```bash
git clone git@github.com:rigozu9/ot-harjoitustyo.git
```
2. Asenna riippuvuudet komennolla:

```bash
poetry install
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
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