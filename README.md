Część B: Instrukcje dla OSOBY, KTÓRA OTRZYMA PLIK (Jak uruchomić projekt)
Oto instrukcja, którą możesz wysłać razem z plikiem ZIP.

Krok 1: Wymagania Wstępne
Upewnij się, że na Twoim komputerze zainstalowany jest Python. Możesz go pobrać ze strony python.org. Podczas instalacji zaznacz opcję "Add Python to PATH".

Krok 2: Rozpakuj projekt
Rozpakuj otrzymany plik ZIP w dowolnej, łatwo dostępnej lokalizacji na swoim komputerze (np. na Pulpicie lub w folderze C:\Projekty).

Krok 3: Otwórz terminal w folderze projektu
Wejdź do rozpakowanego folderu projektu (tego, w którym znajduje się plik manage.py) i otwórz w nim terminal (wiersz poleceń).

Wskazówka dla Windows: W Eksploratorze Plików kliknij w pasek adresu, wpisz cmd i wciśnij Enter.
Krok 4: Stwórz i aktywuj środowisko wirtualne
To kluczowy krok, który izoluje zależności tego projektu od innych.

W terminalu wpisz komendę, aby stworzyć środowisko o nazwie venv:
Bash

python -m venv venv
Następnie aktywuj to środowisko.
Dla Windows:
Bash

.\venv\Scripts\activate
Po tej komendzie na początku linii w terminalu powinien pojawić się napis (venv).
Krok 5: Zainstaluj wszystkie zależności
Teraz użyjemy pliku requirements.txt, aby automatycznie zainstalować Django i inne potrzebne pakiety.

W terminalu z aktywnym środowiskiem ((venv)) wpisz:
Bash

pip install -r requirements.txt
Poczekaj, aż wszystkie pakiety zostaną pobrane i zainstalowane.
Krok 6: Stwórz bazę danych
Projekt nie zawiera bazy danych, więc musimy ją stworzyć na podstawie modeli.

W terminalu wpisz:
Bash

python manage.py migrate
Ta komenda stworzy nowy plik db.sqlite3 i skonfiguruje wszystkie potrzebne tabele.
Krok 7: Uruchom serwer!
Wszystko jest gotowe. Czas uruchomić aplikację.

W terminalu wpisz:
Bash

python manage.py runserver
Otwórz przeglądarkę internetową i wejdź na adres: http://127.0.0.1:8000/.
Strona powinna się załadować i wszystkie funkcje powinny działać.
Uwaga: Ponieważ baza danych jest nowa i pusta, aby się zalogować lub testować funkcje wymagające użytkownika, trzeba będzie najpierw stworzyć nowego użytkownika przez formularz rejestracji.
