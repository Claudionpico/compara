# Start compare

# ******** Init DB  ********
#
#  1 - cd  compare-db
#  2 - make build
#  3 - make run
#
#
#
## ******** Config and init API  ********
#   1 - cd compare-api
#   2 - vim Enviroment --> set ip address of my pc in DB_HOST
#   3 - make build
#   4 - make run /or make dev --> ./run
#
#
# ******** Init compare web  ********
#
#   1 - cd compare-web
#   2 - yarn install
#   3 - yarn run
#
# ********** info **********
#
#   * Load db in compara-api/src/api/__init__.py line 59
#   * Endpoint configured
#       - GET 0.1/cars
#       - POST 0.1/cars
#       - PATCH 0.1/cars
#       - DELETE 0.1/cars
#    Document api compare.postman_collection.json
# 
#   * Database
#   * +----+-------+--------+
#   | id | name  | plate  |
#   +----+-------+--------+
#   |  1 | Corsa | LME456 |
#   |  2 | ARGO  | AAA123 |
#   |  3 | UP    | LRR456 |
#   |  4 | FOX   | HDO222 |
#   +----+-------+--------+
#
#   * Technology used
#      API [flask - python2.7 - sqlalchemy - flask_restless]
#      DB [mysql]
#      WEW [React - React-bootstrap]
