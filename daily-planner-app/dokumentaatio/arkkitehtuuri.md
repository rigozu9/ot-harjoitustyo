# Arkkitehtuurikuvaus

## Rakenne
Ohjelman pakkausrakenne koostuu, sqlalchemy malleista entities kansiossa, repositories kansiosta, josta tehdään tietokantaan liittyvät toiminnot,
services folderista, jossa on sovelluslogiikka ja UI kansiosta, jossa on frontend.
![Pakkausrakenne](./kuvat/pakkausrakenne.png)

## Käyttöliittymä
Käyttöliittymässä on 8 näkymää
- Uuden käyttäjän luominen
- Kirjautuminen
- Daily planner näkymä
- Kalenteri näkymä
- Ensikyselyn näkymä
- Today view, eli päivän aktiviteettien näkymä
- User info view, eli omien tietojen näkymä.
- Advice view mistä näkee omia ehdotuksia.

Näkymillä on omat luokkansa, jotka kutsuvat dailyplanner ja user servicejä. 
Kun näkymää vaihdetaan kutsutaan views sanakirjaa, jossa on ui.py:ssä alusetetut näkymät. 

## Sovelluslogiikka
### Mallit 
[User](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/src/entities/user.py) ja [DailyPlan](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/src/entities/dailyplan.py) muodostavat sovelluksen mallit. User kuvaa käyttäjie ja dailyplan näiden käyttäjien päivittäisiä tekemisiä. 

### Sekvenssikaavio
```mermaid
classDiagram
    class User {
      +int id
      +string username
      +string password
      +int age
      +string sex
      +int sleep
      +bool first_login_completed
    }
    
    class DailyPlan {
      +int id
      +int user_id
      +date date
      +int sleep
      +int outside_time
      +int productive_time
      +int exercise
      +int screen_time
      +string other_activities
    }

    User --> DailyPlan: has
```

### Services ja repositories
[UserService](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/src/services/user_service.py) ja [DailyPlanService](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/src/services/dailyplan_service.py) muodostavat sovelluksen logiikan.


[UserRepository](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/src/repositories/user_repository.py) ja [DailyPlanRepository](https://github.com/rigozu9/ot-harjoitustyo/blob/main/daily-planner-app/src/repositories/dailyplan_repository.py) muodostavat sovelluksen tietokannan tehtävät. 
### Sekvenssikaavio
```mermaid
classDiagram
    class UserService {
        +user_repository
        +__init__(user_repository)
        +register_user(username, password) 
        +login_user(username, password) 
        +get_username(user_id) 
        +is_first_login(user_id) 
        +complete_first_login(user_id)
        +add_info(age, sex, sleep, user_id)
        +show_info(user_id) 
    }

    class UserRepository {
        +__init__(session)
        +find_by_username(username) 
        +create_user(username, password) 
        +verify_user(username, password) 
        +find_id_by_username(username) 
        +get_username_by_user(user_id) 
        +check_first_login(user_id) 
        +complete_first_login_process(user_id)
        +create_info(age, sex, sleep, user_id)
        +get_info(user_id) 
    }

    class DailyPlanService {
        +dailyplan_repository
        +__init__(dailyplan_repository)
        +create_plans(user_id, date, sleep, outsidetime, productivetime, exercisetime, screentime, other)
        +get_plans_by_id(user_id, date)
    }

    class DailyPlanRepository {
        +__init__(session)
        +add_plans(user_id, date, sleep, outsidetime, productivetime, exercisetime, screentime, other)
        +get_plan_from_db(user_id, date) DailyPlan
    }

    UserService --> UserRepository
    DailyPlanService --> DailyPlanRepository
```

## Tietokannan käyttö
Sovellus käyttää sqliteä tietokantana. Siellä on pöydät käyttäjille ja dailyplaneille. 
dailyplan_repository ja user_repository tekevät muutokset tietokantaan ja services kutsuu niitä.
Testien aikana laitetaan test env muuttuja päälle ja silloin käytetään eri tietokantaa kuin normaalisti sovelluksessa.