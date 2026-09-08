:white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s9e02-django-models-and-forms` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#03` Django: Modele oraz formularze

Twoim zadaniem jest stworzenie formularza Django, który nie korzysta z żadnego modelu – będzie to zwykła klasa `forms.Form`, służąca do przesyłania wiadomości kontaktowej.

W tym zadaniu nie tworzysz modeli i nie zapisujesz danych do bazy danych.

## Zakres zadania

- Stwórz formularz `ContactForm` jako podklasę `forms.Form`.
- Formularz ma zawierać dwa pola:
  - `email` – pole typu `EmailField`, wymaga poprawnego adresu e-mail,
  - `message` – pole typu `CharField` z `TextArea`, minimum 20 znaków.

- Utwórz widok, który:
  - dla metody GET wyświetla formularz, Co
  - dla metody POST sprawdza poprawność danych i:
    - jeśli dane są poprawne, wyświetla komunikat „Dziękujemy za wiadomość!”,
    - jeśli dane są błędne, wyświetla formularz ponownie z informacjami o błędach.

## Co powinno znaleźć się w Twoim projekcie?

### Plik `forms.py`

W nim zdefiniuj formularz `ContactForm`

### Plik `views.py`

Utwórz widok `contact_view`, który:

* obsługuje zarówno metodę GET, jak i POST,
* dla poprawnych danych przekazuje do szablonu zmienną `success=True`,
* dla błędnych danych przekazuje formularz z błędami.

### Plik `urls.py`

Dodaj ścieżkę URL `/contact/` i połącz ją z widokiem `contact_view`.

### Szablon `contact.html`

Utwórz formularz HTML z wykorzystaniem tokena CSRF:

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Wyślij</button>
</form>

{% if success %}
    <p style="color: green;">Dziękujemy za wiadomość!</p>
{% endif %}
```

## Testowanie

1. Uruchom serwer (`python manage.py runserver`).
2. Wejdź pod adres `http://127.0.0.1:8000/contact/`.
3. Wypełnij formularz:

   * podaj niepoprawny e-mail → powinien pojawić się błąd,
   * wpisz krótką wiadomość → powinien pojawić się błąd,
   * podaj poprawne dane → powinien pojawić się komunikat podziękowania.

## Twoje rozwiązanie powinno zawierać

* formularz `ContactForm` jako klasa `forms.Form`,
* widok `contact_view` do obsługi formularza,
* szablon `contact.html` z formularzem i komunikatem,
* wpis w `urls.py` ze ścieżką `/contact/`,
* działającą walidację.


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-django-models-and-forms)*

> :arrow_left: [*poprzednie zadanie*](./../02) | [*następne zadanie*](./../04) :arrow_right:
