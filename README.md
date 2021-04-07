# **FastAPI Practice Project**

처음에 .env가 없으니 .env.example가져다가 맞춰서 쓸 것

fastapi-realworld-example-app: [Structure 참고 링크](https://github.com/nsidnev/fastapi-realworld-example-app)  
PEP8: [Coding convention 참고 링크](https://www.python.org/dev/peps/pep-0008/)

Get Started
-----------

    $ source venv/bin/activate
    $ uvicorn main:app

Project structure
-----------------

Files related to application are in the ``app`` or ``tests`` directories. Application parts are:

    app
    ├── api              - web related stuff.
    │   ├── dependencies - dependencies for routes definition.
    │   ├── errors       - definition of error handlers.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── db               - db related stuff.
    │   ├── migrations   - manually written alembic migrations.
    │   └── repositories - all crud stuff.
    ├── models           - pydantic models for this application.
    │   ├── domain       - main models that are used almost everywhere.
    │   └── schemas      - schemas for using in web routes.
    ├── resources        - strings that are used in web responses.
    ├── services         - logic that is not just crud related.
    └── main.py          - FastAPI application creation and configuration.


어떤것이 적용 되어있는가?
------------------
1. [Repository Pattern](https://www.cosmicpython.com/book/chapter_02_repository.html)
2. ...
    