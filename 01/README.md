> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s9e02-django-models-and-forms` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#01` Django: Modele oraz formularze


Twoim zadaniem jest stworzenie modelu Django reprezentującego **produkt**, który może być oferowany w sklepie internetowym.

Skupiamy się tutaj wyłącznie na warstwie modelu – nie musisz tworzyć widoków ani szablonów.

## Zakres zadania

- Zdefiniuj model `Product` w pliku `models.py`.
- Użyj różnych typów pól oraz odpowiednich atrybutów (`default`, `null`, `blank`, `validators`).
- Zarejestruj model w panelu administracyjnym.
- Przetestuj działanie modelu w Django Shell.

## Co powinno znaleźć się w Twoim modelu?

### Model `Product`:

- `id` – automatyczny identyfikator generowany przez Django.
- `name` – nazwa produktu (tekst, wymagane).
- `price` – cena produktu (liczba zmiennoprzecinkowa, większa od 0).
- `in_stock` – czy produkt jest dostępny (wartość logiczna, domyślnie `True`).
- `available_until` – data ważności produktu (może być pusta – `null=True`, `blank=True`).

Dodaj metodę `__str__`, która zwróci informację w formacie:

**`"Nazwa – 199.99 zł"`** 

## Wskazówki

- Do walidacji ceny użyj własnej funkcji walidatora, która sprawdzi, czy wartość jest większa od zera.
- Przykładowy walidator można umieścić w tym samym pliku lub oddzielnym module.


## Testowanie modelu

1. Przeprowadź migrację:

   * `python manage.py makemigrations`
   * `python manage.py migrate`

2. Uruchom Django Shell:

   * `python manage.py shell`

3. Utwórz przykładowy produkt i sprawdź działanie metody `__str__`:

```python
from sklep.models import Product
p = Product.objects.create(name="Buty", price=199.99)
print(p)  # powinno wypisać: Buty – 199.99 zł
```


## Twoje rozwiązanie powinno zawierać

* Model `Product` w pliku `models.py`.
* Walidator sprawdzający cenę.
* Test działania modelu w Django Shell (przeprowadź samodzielnie).


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-django-models-and-forms)*

> :arrow_left: ~~*poprzednie zadanie*~~ | [*następne zadanie*](./../02) :arrow_right:
