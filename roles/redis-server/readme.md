# Redis Server Role for Ansible

Important details regarding the configuration:

 - This role will support multi deployments on a single host this is facilitated by deploying configurations, logs, pids and init scripts in the following manners:
    - /var/log/redis/redis-{port}.log
    - /var/run/redis/{port}.pid
    - /etc/redis/{port}.conf
    - /etc/init.d/redis-{port}
