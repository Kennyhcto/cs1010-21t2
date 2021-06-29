# 4.4 Retrieving data from external sources

## Client libraries
A client library is a library designed to let you communicate with an external service.

**Important Points:**

* Once installed, you can use them anywhere in your Python code.
* They are typically the easiest way to get data from an online service.
* Python has many client libraries, so it's always worth checking if one exists before going to the effort of doing it yourself.

**Examples:**
* ``1_eds_client.py``

## Requests library
The Python requests library allows us to make HTTP requests in much the same way our web browsers do.

**Important points:**

* If you need to communicate with an external service, and there isn't a client library for it, requests is the next best solution.
* We typically use the get() function, but there exists a post() function as well.
* The result of the get() function is a response. The contents of a response are bytes representing the response data.

**Examples:**
* ``2_eds_requests.py``

## APIs
Application Programming Interfaces (APIs) define how different software components communicate.

Web APIs are typically web servers that are designed to receive requests from programs rather than a user navigating with their browser.

**Examples:**
* ``3_eds_api.py``
* ``4_eds_api.py``

**Some Free (to some extent) APIs:**
* https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/
* https://rapidapi.com/marketplace
* https://github.com/public-apis/public-apis
* https://apilist.fun/
* http://deckofcardsapi.com/