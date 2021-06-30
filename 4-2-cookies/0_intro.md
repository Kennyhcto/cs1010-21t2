## Cookies

* Cookies are small pieces of information sent by the server to the web browser in HTTP responses. These pieces of information are then sent back to the server every time the browser makes a new request.

* In flask, the best way to create cookies is with `session`.

**Examples of data to store in a session:**
* Items in a user's shopping cart
* Whether the user is logged in or not
* Preferences (language, currency, dark vs. light mode)

**Examples of data to store in a database (not covered for now):**
* User credentials (email, username, hashed password, email confirmed boolean)
* Data entered by the user (stock data, recipes, blog posts)

**Keywords:**
* `from flask import session`
* `app.config['SECRET_KEY'] = 'random_long_unguessable_string'`
* `if 'key' in session:`
* `value = session.get('key', default_value)`
* `session['key'] = 'value'`
* `session.modified = True`

**Generating a random secret key:**

```python
import secrets
secrets.token_urlsafe(16)
```
