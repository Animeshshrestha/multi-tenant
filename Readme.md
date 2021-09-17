# Multi-tenant architecture software base

This application is powered by django along with django tenant schemas to have multiple tenants via **PostgreSQL schemas**.

Basically, Tenants are identified via their host name(i.e. tenant.domain.com) but in this project we are identifying the tenant via the **api-key header** present in request headers. Each tenant can have more than one unique api-key which is stored in the database.

<u>Technologies Used</u>

- Backend: Python, Django, Postgresql
- Deploymment tools: Docker, nginx

# Project Features:

1. Create Tenant and Api-Key for that respective tenant.
2. User Registration with User Login System.
3. CRUD operation of User Posts.

# Project Installation

1. Extract the code if its in zip format
2. Setup the virtual environment
3. Run the command

```bash
pip install -r requirements.txt
```

4. For the database configuration please refer to the .envs file located under the folder **/.envs/.local/** for the respective variables for django and postgres respectively.
5. <u> Want to run via docker </u>: Use the following command

```bash
docker-compose -f local.yml build
docker-compose -f local.yml up -d
```

Visit <u> localhost:8000 or 0.0.0.0:8000 </u> if you are using docker-compose

[Swagger API List Documentation](http://localhost:8000/swagger/)

# Creating Tenant and generating api-key for the respective tenant

1. To create tenant at first open up the shell powered by django

```bash
python3 manage.py shell
```

2. Import the tenant models app and create tenant object along with Api-Key.

```bash
from app.tenants.models import Tenant
from app.api_key.models import ApiKey
tenant = Tenant.objects.create(name="Test Tenant", address="Tenant Address", schema_name="test_tenant")
api_key = ApiKey.objects.create(agency=tenant)
<ApiKey: ebwX8QiJmi6DldUPeIV2WNIzpv8olzyb0ZWcMeq1>
```

3. Now pass **ebwX8QiJmi6DldUPeIV2WNIzpv8olzyb0ZWcMeq1** as api-key value in request headers. <mark> i.e:{'api-key':'ebwX8QiJmi6DldUPeIV2WNIzpv8olzyb0ZWcMeq1'} </mark>

Note: If you are using docker then run the following command so that you can get access to the shell

```bash
docker-compose -f local.yml run --rm web python manage.py shell
```

and follow the above mentioned steps to create the tenants and api-key.

# Known Bugs:

1. Make sure to append the trailing slash to the url or else you can encounter errors.
2. While running the docker compose up you might get following errors:
   1. If you have already run the postgres server on your local machine then the postgres might not be connected to docker which may prompt you to error.
      To resolve this make sure to change the exposed port or stop the running postgres services on your localhost machine.
      **Error Type**:
      Cannot start service db: driver failed programming external connectivity on endpoint. Error starting userland proxy: listen tcp4 0.0.0.0:5432: bind: address already in use
