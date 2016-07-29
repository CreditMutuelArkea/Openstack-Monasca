# Installation

Steps :

| Name of the component | Version |
| -- | -- |
| Install and configure ZooKeeper | 3.4.8 |
| Install and configure Kafka | 0.9.0.1 |
| Install and configure InfluxDB | 0.10.3-1 |
| Install and configure Storm | 0.9.6-1 |
| Configure Mysql | - |
| Configure Keystone| - |
| Install and configure Monasca-UI  | 1.0.31-1 |
| Install and configure Monasca-API  | 1.1.2-1 |
| Install and configure Monasca-Persister |  0.1.15 |
| Install and configure Monasca-Thresh | 0.0.2-1 |
| Install and configure Monasca-Notification | 1.2.13-1 |
| Install and configure Monasca-Agent | 1.1.24-1 |


## Packages

I can't use Pypi for installing the Monasca's components and i can't just extract archives files for ZooKeeper or Kafka so i use the way of Arkea doing installation : Packages.

All the specfile are on [GitHub](https://github.com/TomEros/Openstack-Monasca). 

We use Centos with the Mitaka repository and it was needed to build all that packages :

* Kafka
* Monasca-grafana
* Monasca-thresh
* Python-argparse
* Python-dateutil
* Python-gearman
* Python-gunicorn
* Python-influxdb
* Python-kafka
* Python-monasca-agent
* Python-monasca-api
* Python-monasca-common
* Python-monasca-notification
* Python-monasca-persister
* Python-monasca-statsd
* Python-monasca-ui
* Python-monascaclient
* Python-monotonic
* Python-nose-cov
* Python-pastedeploy
* Python-simport
* Python-statsd
* Python-ujson
* Python-validate-email
* Storm
* Zookeeper










