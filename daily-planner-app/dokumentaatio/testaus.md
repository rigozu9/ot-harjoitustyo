# Testausdokumentti

Sovellusta on testattu python unittestien avulla, windowsin koneella ja fuksiläppärillä.

## Yksikkö- ja integraatiotestaus

Sovelluslogiikan testeissä on 2 eri tiedostoa. [User](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/src/tests/user/test_user.py) ja [Dailyplan](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/src/tests/daily_planner/test_dailyplan.py). 
User tiedosto vastaa käyttäjä tehtävien testaamisesta ja dailyplan taas dailyplanien tehtävistä.

### Testauskattavuus

Testauksen haarautumakattavuus on 96%

![](./kuvat/testikattavuus.png)


## Järjestelmätestaus ja asennus

Sovellusta on testattu [käyttöohjeen](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/dokumentaatio/kayttoohje.md) avulla ja myös kloonaamalla repositori koneelle. Näitä on testattu windowsin koneella ja myös linuxin fuksiläppärillä. Sovellus toimi kuten pitääkin.