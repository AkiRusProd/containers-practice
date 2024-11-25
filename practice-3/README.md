# Практика 3: Kubernetes

## Отчет по заданию
1. Запуск minikube
![alt text](images/image.png)
Исправляем проблему с доступом `https://registry.k8s.io` командой `sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf':     
`:      
![alt text](images/fix_minikube.png)

2. Проверка установки
![alt text](images/check_install.png)

3. Создание объектов из манифестов
![alt text](images/create.png)

4. Проверка     
![alt text](images/check1.png)
![alt text](images/check2.png)
![alt text](images/check3.png)
![alt text](images/nc_log.png)
![alt text](images/nc_expose.png)

5. Туннелирование трафика
![alt text](images/tun.png)

6. Переход по ссылке
![alt text](images/url.png)

6. Дэшборд