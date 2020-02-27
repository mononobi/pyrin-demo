# Pyrin-Demo

Demo application developed using Pyrin framework.

# Running

You could run the application by executing the following command:

**`python3 start.py`**

Application will be available at **`127.0.0.1:9081`** by default.

# Configurations

Application will use Pyrin's default configurations, including an **`in-memory sqlite`** 
database. If you want to change any configuration, you could change it inside 
**`src/demo/settings`**

# Exposed Services

Demo application will expose these services:

- Public

    - `('/security/users/create', methods=HTTPMethodEnum.POST, login_required=False)`
    - `('/security/login', methods=HTTPMethodEnum.POST, login_required=False)`
    - `('/common/city/create', methods=HTTPMethodEnum.POST, login_required=False)`
    - `('/common/city/get/<int:city_id>', methods=HTTPMethodEnum.GET, login_required=False)`
    - `('/common/city/find', methods=HTTPMethodEnum.GET, login_required=False)`
    - `('/common/province/create', methods=HTTPMethodEnum.POST, login_required=False)`
    - `('/common/province/get/<int:province_id>', methods=HTTPMethodEnum.GET, login_required=False)`
    - `('/common/province/find', methods=HTTPMethodEnum.GET, login_required=False)`
    - `('/common/province/get_all', methods=HTTPMethodEnum.GET, login_required=False)`

- Protected (Requires Login and Authorization Header with Access Token)

    - `('/security/users/get', methods=HTTPMethodEnum.GET)`
    - `('/security/users/get_all', methods=HTTPMethodEnum.GET, permissions=VIEW_USERS_LIST_PERMISSION)`
