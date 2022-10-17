# VPS API-based management

## Управление выделенными серверами с помощью API

### Объект VPS
- uid - идентификатор
- cpu - количество ядер
- ram - объем RAM
- hdd - объем HDD
- status - статус сервера (started, blocked, stopped)

### API поддерживает операции
- создать VPS
- получить VPS по uid
- получить список VPS с возможностью фильтрации по параметрам
- перевести VPS в другой статус

## Примеры запросов

- Получить список доступных VPS

    ```GET /api/v1/vps```
    
- Создать VPS

    ```POST /api/v1/vps```
    
- Обновить полностью VPS

    ```PUT /api/v1/vps```
    
- Обновить частично VPS

    ```PATCH /api/v1/vps```
    
- Удалить VPS

    ```DELETE /api/v1/vps```

- Получить VPS по uuid

    ```POST /api/v1/vps/get-vps-by-uuid/```
    
- Изменить статус VPS

    ```POST /api/v1/vps/change-status/```
    
- Получить список лучших VPS

    ```POST /api/v1/vps/get-best-vps/```
    
- Зарегистрировать нового пользователя

    ```POST /auth/users/```
    
- Получить информацию об авторизованном пользователе

    ```POST /auth/users/me/```
    
- Получить токен

    ```POST /auth/jwt/create/```

- Обновить токен

    ```POST /auth/jwt/refresh/```
