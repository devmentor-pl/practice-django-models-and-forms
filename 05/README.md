> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s9e02-django-models-and-forms` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#05` Django: Modele oraz formularze

Twoim zadaniem jest skonfigurowanie panelu administracyjnego Django dla modelu `Product`. Celem zadania jest nauczenie się jak dostosować widok listy obiektów oraz jak dodać niestandardową akcję.

## Zakres zadania

- Zarejestruj model `Product` w panelu administracyjnym.
- Skonfiguruj widok listy (`list_display`), aby wyświetlał kluczowe informacje.
- Dodaj akcję, która obniża cenę wybranych produktów o 10%.

## Co powinno znaleźć się w Twoim projekcie?

### Model `Product`:

Załóż, że masz już model `Product` z następującymi polami:
- `name` – nazwa produktu (tekst),
- `price` – cena produktu (liczba zmiennoprzecinkowa),
- `in_stock` – wartość logiczna.

### Plik `admin.py`

Zarejestruj model `Product` z własną klasą administracyjną oraz dodaj odpowiednią akcję np `"discount_10_percent"`.

Przykładowo: 

```python
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_stock']
    
    actions = ['discount_10_percent']
...
````

### Testowanie

1. Uruchom serwer deweloperski.
2. Przejdź do panelu admina: `http://127.0.0.1:8000/admin/`.
3. Dodaj kilka produktów ręcznie.
4. Zaznacz produkty na liście i z menu akcji wybierz „Obniż cenę o 10%”.
5. Upewnij się, że ceny produktów zostały zaktualizowane.

## Twoje rozwiązanie powinno zawierać

* rejestrację modelu `Product` w pliku `admin.py`,
* konfigurację `list_display` dla pól `name`, `price`, `in_stock`,
* definicję akcji administracyjnej `discount_10_percent`,
* test działania akcji w panelu administracyjnym (wykonany samodzielnie).



&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-django-models-and-forms)*

> :arrow_left: [*poprzednie zadanie*](./../04) | ~~*następne zadanie*~~ :arrow_right:
