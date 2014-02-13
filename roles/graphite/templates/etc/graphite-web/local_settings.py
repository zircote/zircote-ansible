## Graphite local_settings.py

#####################################
# General Configuration #
#####################################
{% if graphite_config_general.secret_key is defined %}
SECRET_KEY = '{{ graphite_config_general.secret_key }}'
{% endif %}{% if graphite_config_general.allowed_hosts is defined %}
ALLOWED_HOSTS = {{ graphite_config_general.allowed_hosts }}
{% endif %}{% if graphite_config_general.time_zone is defined %}
TIME_ZONE = '{{ graphite_config_general.time_zone }}'
{% endif %}{% if graphite_config_general.documentation_url is defined %}
DOCUMENTATION_URL = "{{ graphite_config_general.documentation_url }}"
{% endif %}{% if graphite_config_general.log_rendering_performance is defined %}
LOG_RENDERING_PERFORMANCE = {{ graphite_config_general.log_rendering_performance | bool }}
{% endif %}{% if graphite_config_general.log_cache_performance is defined %}
LOG_CACHE_PERFORMANCE = {{ graphite_config_general.log_cache_performance | bool }}
{% endif %}{% if graphite_config_general.log_metric_access is defined %}
LOG_METRIC_ACCESS = {{ graphite_config_general.log_metric_access }}
{% endif %}{% if graphite_config_general.debug is defined %}
DEBUG = {{ graphite_config_general.debug | bool }}
{% endif %}{% if graphite_config_general.flushrrdcached is defined %}
FLUSHRRDCACHED = '{{ graphite_config_general.flushrrdcached }}'
{% endif %}{% if graphite_config_general.memcache_hosts is defined %}
MEMCACHE_HOSTS = {{ graphite_config_general.memcache_hosts }}
{% endif %}{% if graphite_config_general.default_cache_duration is defined %}
DEFAULT_CACHE_DURATION = {{ graphite_config_general.default_cache_duration | int}}
{% endif %}


#####################################
# Filesystem Paths #
#####################################
{% if graphite_config_paths.graphite_root is defined %}
GRAPHITE_ROOT = '{{ graphite_config_paths.graphite_root }}'
{% endif %}{% if graphite_config_paths.conf_dir is defined %}
CONF_DIR = '{{ graphite_config_paths.conf_dir }}'
{% endif %}{% if graphite_config_paths.storage_dir is defined %}
STORAGE_DIR = '{{ graphite_config_paths.storage_dir }}'
{% endif %}{% if graphite_config_paths.content_dir is defined %}
CONTENT_DIR = '{{ graphite_config_paths.content_dir }}'
{% endif %}
{% if graphite_config_paths.dashboard_conf is defined %}
DASHBOARD_CONF = '{{ graphite_config_paths.dashboard_conf }}'
{% endif %}{% if graphite_config_paths.graphtemplates_conf is defined %}
GRAPHTEMPLATES_CONF = '{{ graphite_config_paths.graphtemplates_conf }}'
{% endif %}

## Data directories
WHISPER_DIR = '{{ graphite_config_paths.whisper_dir }}'
RRD_DIR = '{{ graphite_config_paths.rrd_dir }}'
DATA_DIRS = [WHISPER_DIR, RRD_DIR]
LOG_DIR = '{{ graphite_config_paths.log_dir }}'
INDEX_FILE = '{{ graphite_config_paths.index_file }}'


#####################################
# Email Configuration #
#####################################
{% if graphite_config_email.email_backend is defined %}
EMAIL_BACKEND = '{{ graphite_config_email.email_backend }}'
{% endif %}{% if graphite_config_email.email_hosts is defined %}
EMAIL_HOST = '{{ graphite_config_email.email_hosts }}'
{% endif %}{% if graphite_config_email.email_port is defined %}
EMAIL_PORT = {{ graphite_config_email.email_port|int }}
{% endif %}{% if graphite_config_email.email_host_user is defined %}
EMAIL_HOST_USER = '{{ graphite_config_email.email_host_user }}'
{% endif %}{% if graphite_config_email.email_host_password is defined %}
EMAIL_HOST_PASSWORD = '{{ graphite_config_email.email_host_password }}'
{% endif %}{% if graphite_config_email.email_use_tls is defined %}
EMAIL_USE_TLS = {{ graphite_config_email.email_use_tls }}
{% endif %}

#####################################
# Authentication Configuration #
#####################################
{% if graphite_config_auth.ldap_uri is defined %}
LDAP_URI = "{{ graphite_config_auth.ldap_uri }}"
{% endif %}{% if graphite_config_auth.ldap_search_base is defined %}
LDAP_SEARCH_BASE = "{{ graphite_config_auth.ldap_search_base }}"
{% endif %}{% if graphite_config_auth.ldap_base_user is defined %}
LDAP_BASE_USER = "{{ graphite_config_auth.ldap_base_user }}"
{% endif %}{% if graphite_config_auth.ldap_base_pass is defined %}
LDAP_BASE_PASS = "{{ graphite_config_auth.ldap_base_pass }}"
{% endif %}{% if graphite_config_auth.ldap_user_query is defined %}
LDAP_USER_QUERY = "{{ graphite_config_auth.ldap_user_query }}"
{% endif %}

{% if graphite_config_auth.ldap_optional_script is defined %}
{{ graphite_config_auth.ldap_optional_script }}
{% endif %}{% if graphite_config_auth.use_remote_user_authentication is defined %}
USE_REMOTE_USER_AUTHENTICATION = {{ graphite_config_auth.use_remote_user_authentication|bool }}
{% endif %}{% if graphite_config_auth.login_url is defined %}
LOGIN_URL = '{{ graphite_config_auth.login_url }}'
{% endif %}


##########################
# Database Configuration #
##########################

{% if graphite_config_database.databases is defined %}
DATABASES = {{ graphite_config_database.databases }}
{% endif %}

#########################
# Cluster Configuration #
#########################
{% if graphite_config_cluster.cluster_servers is defined %}
CLUSTER_SERVERS = {{ graphite_config_cluster.cluster_servers }}
{% endif %}

{% if graphite_config_cluster.remote_store_fetch_timeout is defined %}
REMOTE_STORE_FETCH_TIMEOUT = {{ graphite_config_cluster.remote_store_fetch_timeout | int}}
{% endif %}{% if graphite_config_cluster.remote_store_find_timeout is defined %}
REMOTE_STORE_FIND_TIMEOUT = {{ graphite_config_cluster.remote_store_find_timeout | int}}
{% endif %}{% if graphite_config_cluster.remote_store_retry_delay is defined %}
REMOTE_STORE_RETRY_DELAY = {{ graphite_config_cluster.remote_store_retry_delay }}
{% endif %}{% if graphite_config_cluster.remote_find_cache_duration is defined %}
REMOTE_FIND_CACHE_DURATION = {{ graphite_config_cluster.remote_find_cache_duration }}
{% endif %}

## Remote rendering settings
{% if graphite_config_cluster.remote_rendering is defined %}
REMOTE_RENDERING = {{ graphite_config_cluster.remote_rendering | bool }}
{% endif %}{% if graphite_config_cluster.rendering_hosts is defined %}
RENDERING_HOSTS = {{ graphite_config_cluster.rendering_hosts }}
{% endif %}{% if graphite_config_cluster.remote_render_connect_timeout is defined %}
REMOTE_RENDER_CONNECT_TIMEOUT = {{ graphite_config_cluster.remote_render_connect_timeout | int }}
{% endif %}{% if graphite_config_cluster.carbonlink_hosts is defined %}
CARBONLINK_HOSTS = {{ graphite_config_cluster.carbonlink_hosts }}
{% endif %}{% if graphite_config_cluster.carbonlink_timeout is defined %}
CARBONLINK_TIMEOUT = {{ graphite_config_cluster.carbonlink_timeout | int }}
{% endif %}

#####################################
# Additional Django Settings #
#####################################

# from graphite.app_settings import *
