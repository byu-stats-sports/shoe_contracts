# shoe_contracts

Downloads data using the [stats.nba.com](http://stats.nba.com) API via the [nba_py](https://github.com/seemethere/nba_py) package, as well as [nbashoesdb.com](http://nbashoesdb.com) as a webscrape and updates the MySQL database designated by the `BYU_NBA_DATABASE_URL` environment variable using the [peewee](http://docs.peewee-orm.com/en/latest/) database Object Relational Map (ORM). 

## requirements 

 - [`python`](http://docs.python-guide.org/en/latest/starting/installation/)
 - [`pip`](https://pip.pypa.io/en/stable/installing/)
 - [`git`](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
 
## usage

1. Fire up your terminal

1. Configure (export) the database setting, replacing `<user>`, `<password>`, `<host>` with the appropriate values:

  Add `export BYU_NBA_DATABASE_URL="mysql://<user>:<password>@<host>/nba"` to your `~/.bash_profile`:

  ```
  echo 'export BYU_NBA_DATABASE_URL="mysql://<user>:<password>@<host>/nba"' >> ~/.bash_profile
  ``` 
  
  _NOTE_: You may also want to export `NBA_PY_CACHE_EXPIRE_MINUTES` to something more than the default `10` so that you don't have to download NBA data as much. 
  
1. Ensure that you have [`pip`](https://pip.pypa.io/en/stable/installing/) and [`git`](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed

1. Install the app:
  
  ```
  pip install git+https://github.com/byu-stats-sports/shoecontracts.git
  ```
  
1. Get help on how to use the app:
  
  ```
  nba --help
  ```

## develop

1. Fire up your terminal

1. Ensure that you have [`git`](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed

1. Download the source:
  
  ```
  git clone https://github.com/byu-stats-sports/shoecontracts.git
  ```
  
1. Install the application: 
  
  ```
  pip install --editable shoecontracts/
  ```
