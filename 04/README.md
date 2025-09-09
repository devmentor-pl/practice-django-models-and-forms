sour> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s9e02-django-models-and-forms` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#04` Django: Modele oraz formularze

Twoim zadaniem jest stworzenie modelu `Article` oraz widoku, który umożliwia filtrowanie artykułów na podstawie zawartości tytułu i daty publikacji.

Celem jest przećwiczenie pracy z modelami, widokami funkcyjnymi i filtrowaniem danych przy użyciu metod `filter()` oraz lookupów Django.

## Zakres zadania

- Zdefiniuj model `Article` z odpowiednimi polami.
- Dodaj widok, który filtruje dane na podstawie parametrów przekazanych w URL.
- Wyniki mają być wyświetlane jako zwykła lista tekstowa (bez HTML).

## Co powinno znaleźć się w Twoim projekcie?

### Model `Article`:

- `id` – identyfikator artykułu.
- `title` – tytuł artykułu (`CharField`, max 200 znaków).
- `content` – treść artykułu (`TextField`).
- `published_at` – data i godzina publikacji (`DateTimeField`).

Dodaj metodę `__str__()`, która zwraca `title`.

### Widok `recent_django_articles`

Stwórz widok, który:
- wyszukuje tylko te artykuły, których tytuł zawiera słowo „Django” (niezależnie od wielkości liter),
- oraz zostały opublikowane po 1 stycznia 2024.

Wyniki mają być zwrócone w `HttpResponse`, każdy tytuł w nowej linii.

### Plik `urls.py`

Dodaj ścieżkę URL `/django-recent/`, która wskazuje na widok `recent_django_articles`.

## Testowanie

1. Uruchom Django Shell i dodaj kilka artykułów z różnymi tytułami i datami publikacji.
2. Uruchom serwer i przejdź do adresu `http://127.0.0.1:8000/django-recent/`.
3. Upewnij się, że widzisz tylko artykuły spełniające oba warunki:
   - tytuł zawiera „Django” (np. „Wprowadzenie do Django”, „django w praktyce”),
   - data publikacji jest po 1 stycznia 2024.

## Twoje rozwiązanie powinno zawierać

- model `Article` z polami `title`, `content`, `published_at`,
- metodę `__str__()` w modelu,
- widok `recent_django_articles` z filtrowaniem danych,
- ścieżkę URL `/django-recent/`,
- poprawnie działające filtrowanie po tytule i dacie.



&nbsp;

> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-django-models-and-forms)*

> :arrow_left: [*poprzednie zadanie*](./../03) | [*następne zadanie*](./../05) :arrow_right:
