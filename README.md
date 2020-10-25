# Pyrin-Demo

Demo application developed using Pyrin framework.

# Running

You could run the application by executing the following command:

**`python3 start.py`**

Application will be available at **`127.0.0.1:5000`** by default.

# Configurations

Application will use Pyrin's default configurations, including an **`in-memory sqlite`** 
database. If you want to change any configuration, you could change it inside 
**`src/demo/settings`**

# Exposed Services

Demo application will expose these services:

- Public

    - `('/auth/login', methods=HTTPMethodEnum.POST, authenticated=False)`
    - `('/users', methods=HTTPMethodEnum.POST, authenticated=False)`
    - `('/users', methods=HTTPMethodEnum.GET, authenticated=False)`
    - `('/cities/<int:city_id>', methods=HTTPMethodEnum.GET, authenticated=False)`
    - `('/cities', methods=HTTPMethodEnum.POST, authenticated=False)`
    - `('/cities/find', methods=HTTPMethodEnum.GET, authenticated=False)`
    - `('/provinces/<int:province_id>', methods=HTTPMethodEnum.GET, authenticated=False)`
    - `('/provinces', methods=HTTPMethodEnum.GET, authenticated=False)`
    - `('/provinces', methods=HTTPMethodEnum.POST, authenticated=False)`
    - `('/provinces/find', methods=HTTPMethodEnum.GET, authenticated=False)`

- Protected (Requires Login and Authorization Header with Access Token)

    - `('/users/info', methods=HTTPMethodEnum.GET, permissions=VIEW_USERS_LIST_PERMISSION)`
