# Практика 2: Базовый RAG в докер-контейнере

## Отчет по заданию

### Структура

Docker Compose состоит из 4 сервисов:
1. `ChromaDB` - Векторное хранилище данных
2. `LLM-RAG` - API, представляющее сущность LLM
3. `WebUI` - Web-интерфейс
4. `Init` - Инициализатор базы данных, если она пуста

Все требования к [docker-compose.yml](docker-compose.yml) соблюдены.

### Доступ

API LLM-RAG: http://localhost:9000/docs      
API ChromaDB: http://localhost:8000/docs     
WebUI: http://localhost:7860    

### Результат
![Result](images/webui.png)

### Вопросы:
1. **Можно ли ограничивать ресурсы (например, память или CPU) для сервисов в docker-compose.yml? Если нет, то почему, если да, то как?**    
    Ответ: Да, ограничивать ресурсы для сервисов в docker-compose.yml можно.    
    Пример в Swarm Mode:
    ```yaml
    services:
     my_service:
      image: my_image
      deploy:
        resources:
         limits:
          cpus: '0.5'   # 50% от одного CPU
          memory: 512M  # ограничение памяти в 512 МБ
         reservations:
          cpus: '0.1'   # резерв на 25% CPU
          memory: 256M  # резерв памяти в 256 МБ
    ```
    Пример без Swarm Mode:
    ```yaml
    services:
     my_service:
      image: my_image
      mem_limit: 512m  # ограничение памяти
      cpus: '0.5'      # ограничение CPU
    ```
2. **Как можно запустить только определенный сервис из docker-compose.yml, не запуская остальные?**    
    Ответ: Для запуска определенного сервиса используется ключ команда запуска `docker-compose up` с названием сервиса.     
    Пример:
    ```bash
    docker-compose up my_service
    ```