> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s9e02-django-models-and-forms` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#02` Django: Modele oraz formularze - relacje

Twoim zadaniem jest stworzenie dwóch modeli Django: **kategorii** i **artykułu**, powiązanych ze sobą relacją jeden-do-wielu.

Skupiamy się tutaj na strukturze danych oraz testowaniu relacji w Django Shell.

## Zakres zadania

- Zdefiniuj modele `Category` i `Article` w pliku `models.py`.
- W modelu `Article` użyj pola `ForeignKey`, aby powiązać go z `Category`.
- Przetestuj w Django Shell tworzenie i usuwanie powiązanych danych.

## Co powinno znaleźć się w Twoim projekcie?

### Model `Category`:

- `id` – automatyczny identyfikator tworzony przez Django.
- `name` – nazwa kategorii (unikalna, tekst do 100 znaków).

### Model `Article`:

- `id` – identyfikator artykułu.
- `title` – tytuł artykułu (tekst do 200 znaków).
- `content` – treść artykułu (wielowierszowy tekst).
- `category` – powiązanie z kategorią (`ForeignKey` do modelu `Category`, `on_delete=models.CASCADE`).

Dodaj metodę `__str__()` w obu modelach:
- w `Category` zwróć nazwę kategorii,
- w `Article` zwróć tytuł artykułu.

## Testowanie modelu

1. Przeprowadź migrację:
   - `python manage.py makemigrations`
   - `python manage.py migrate`

2. Uruchom Django Shell:
   - `python manage.py shell`

3. Utwórz przykładowe dane:

```python
from blog.models import Category, Article

c = Category.objects.create(name="Python")
Article.objects.create(title="Wprowadzenie do Pythona", content="...", category=c)
Article.objects.create(title="Zaawansowane typy danych", content="...", category=c)
````

4. Pobierz wszystkie artykuły przypisane do kategorii `"Python"`:

```python
for article in c.article_set.all():
    print(article.title)
```

5. Sprawdź, ile artykułów jest w bazie

```python
Article.objects.count()
```

6. Usuń kategorię `"Python"` i sprawdź, czy artykuły również zostały usunięte

## Twoje rozwiązanie powinno zawierać

* Modele `Category` i `Article` z relacją jeden-do-wielu.
* Metody `__str__()` w obu modelach.
* Przykładowe dane utworzone i sprawdzone w Django Shell.


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-django-models-and-forms)*

> :arrow_left: [*poprzednie zadanie*](./../01) | [*następne zadanie*](./../03) :arrow_right:
