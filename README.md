# Projekt SQL & QA Automation – E-commerce

## O projekcie

Praktyczny projekt z zakresu QA Automation i SQL oparty na przykładowej aplikacji e-commerce.

Projekt pokazuje pracę z relacyjną bazą danych, zapytaniami SQL, integracją bazy danych z Pythonem, testami automatycznymi oraz organizacją pracy projektowej z wykorzystaniem Jira.

## Technologie

* Python
* SQL
* SQLite
* SQLite3
* SQLAlchemy ORM
* Pytest
* FastAPI
* Requests
* REST API
* Git
* Jira

## Cele projektu

* Praktyczne wykorzystanie zapytań SQL na relacyjnej bazie danych
* Analiza danych e-commerce za pomocą SQL
* Praca z SQLite przy użyciu Pythona
* Wykorzystanie SQLAlchemy ORM do komunikacji z bazą danych
* Tworzenie REST API z wykorzystaniem FastAPI
* Tworzenie testów API przy użyciu Pytest i Requests
* Weryfikowanie danych z API względem danych w bazie danych
* Organizacja zadań i procesu testowego z wykorzystaniem Jira
* Praktyczne wykorzystanie Git w procesie tworzenia projektu

## Baza danych

Baza danych zawiera następujące tabele:

* `users`
* `products`
* `orders`
* `order_items`

Relacje pomiędzy tabelami odwzorowują podstawowy proces zakupowy w aplikacji e-commerce.

## SQL

Projekt zawiera zapytania wykorzystujące m.in.:

* SELECT
* WHERE
* LIKE
* IN
* BETWEEN
* ORDER BY
* LIMIT
* JOIN
* GROUP BY
* HAVING
* funkcje agregujące
* UPDATE
* DELETE
* podzapytania
* indeksy
* transakcje

Zapytania SQL służą zarówno do analizy danych, jak i do weryfikacji poprawności danych zapisanych w bazie.

## Python i baza danych

Projekt wykorzystuje dwa sposoby komunikacji z SQLite:

### SQLite3

* nawiązywanie połączenia z bazą
* wykonywanie zapytań SQL
* pobieranie wyników
* parametryzowane zapytania

### SQLAlchemy ORM

* definiowanie modeli tabel jako klas Pythona
* wykonywanie zapytań za pomocą ORM
* tworzenie, odczytywanie, aktualizowanie i usuwanie danych
* wykorzystanie `Session`
* obsługa transakcji

## REST API

Projekt zawiera własne REST API zbudowane w FastAPI, które komunikuje się bezpośrednio z bazą SQLite.

Aktualnie rozwijane są endpointy dla danych użytkowników oraz testy ich działania.

## QA Automation

Testy automatyczne z wykorzystaniem Pytest i Requests sprawdzają m.in.:

* statusy odpowiedzi API
* poprawność danych zwracanych przez API
* poprawność utworzonych rekordów
* poprawność aktualizacji rekordów
* poprawność danych w bazie
* zgodność danych pomiędzy API i bazą danych
* obsługę nieprawidłowych danych
* zachowanie aplikacji w przypadku błędów

Przykładowy przepływ testu:

```text
API request
    ↓
REST API
    ↓
Database
    ↓
SQLAlchemy / SQL
    ↓
Database assertion
    ↓
Pytest
```

## Jira

Jira jest wykorzystywana do organizacji pracy nad projektem.

Przykładowe zadania:

* utworzenie struktury bazy danych
* przygotowanie danych testowych
* przygotowanie zapytań SQL
* implementacja modeli SQLAlchemy
* przygotowanie testów API
* walidacja danych w bazie
* zgłaszanie i dokumentowanie błędów

Przykładowy workflow:

```text
To Do → In Progress → Code Review → Testing → Done
```

Zadania w Jira są powiązane z implementacją i zmianami w repozytorium Git.

## Git

Git jest wykorzystywany do:

* wersjonowania kodu
* tworzenia commitów dla poszczególnych zadań
* pracy na branchach
* dokumentowania zmian

Przykładowy commit:

```text
TASK-5 Add database validation for user creation
```

## Struktura projektu

```text
E-commerce-SQL-QA_Automation-Project/
│
├── api/
│   └── main.py
│
├── database/
│   ├── models.py
│   └── queries.py
│
├── tests/
│   ├── test_users.py
│   └── test_orders.py
│
├── sql/
│   ├── analysis.sql
│   └── reports.sql
│
├── data/
│   └── seed.py
│
├── README.md
└── requirements.txt
```

## Status

🚧 Projekt w trakcie tworzenia
