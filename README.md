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

  ## Instalacja i uruchomienie

* Sklonuj repozytorium i przejdź do katalogu projektu:

   ```powershell
   git clone <adres-repozytorium>
   cd E-commerce_SQL_&_QA_Automation-Project

* Utwórz i aktywuj środowisko wirtualne:

  python -m venv .venv
  .venv\Scripts\Activate.ps1

* Zainstaluj wymagane biblioteki:

pip install -r requirements.txt

* Uruchom API:

python -m uvicorn api.main:app --reload

Po uruchomieniu dokumentacja API będzie dostępna pod adresem:

http://127.0.0.1:8000/docs

* Uruchom testy:

pytest
  
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

Jira została wykorzystana do organizacji pracy nad projektem oraz śledzenia wykonanych
zadań, błędów i dokumentacji.

### Zgłoszenia projektowe

* `KAN-4` — Story: Rozwój projektu E-commerce SQL & QA Automation
* `KAN-5` — Task: Przygotowanie bazy danych SQLite i danych testowych
* `KAN-7` — Task: Przygotowanie zapytań SQL i raportów
* `KAN-8` — Task: Implementacja modeli SQLAlchemy dla zamówień
* `KAN-9` — Task: Dodanie endpointów i testów produktów
* `KAN-10` — Task: Dokumentacja uruchomienia projektu
* `KAN-11` — Bug: Niepoprawny oczekiwany status HTTP w teście tworzenia produktu
* `KAN-12` — Task: Uzupełnienie dokumentacji Jira i Git w README

### Workflow

W projekcie wykorzystano prosty workflow:

```text
To Do → In Progress → Done

Zadania wykonane w projekcie zostały przeniesione do statusu Done.
Zgłoszenie błędu KAN-11 pozostaje w statusie To Do do późniejszego poprawienia.

### Powiązanie Jira z Git

Zmiany w repozytorium są opisywane w commitach zawierających klucz zadania Jira.

Przykłady:

KAN-5 Add SQLite database and seed data
KAN-7 Add SQL analysis and report queries
KAN-8 Add Order and OrderItem SQLAlchemy models
KAN-9 Add product API endpoints and tests
KAN-12 Update Jira and Git documentation

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
