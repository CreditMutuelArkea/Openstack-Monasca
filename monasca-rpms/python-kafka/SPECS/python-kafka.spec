%global upstream_name kafka
%global name kafka-python
%global version 0.9.5
%global release 1

Summary:          Pure Python client for Apache Kafka
Name:             %{name}
Version:          %{version}
Release:          %{release}%{?dist}

License:          ASL 2.0
URL:              https://github.com/dpkp/kafka-python
Source0:          http://pypi.python.org/packages/source/k/%{name}/%{name}-%{version}.tar.gz

BuildArch:        noarch
BuildRequires:    python-setuptools
BuildRequires:    python2-devel
BuildRequires:    python-pbr
BuildRequires:    python-sphinx

Requires:         python-six

%description
This module provides low-level protocol support for Apache Kafka as well as
high-level consumer and producer classes. Request batching is supported by the
protocol as well as broker-aware request routing. Gzip and Snappy compression
is also supported for message sets.

%prep
%setup -q 

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst
%{python2_sitelib}/kafka
%{python2_sitelib}/*.egg-info

%changelog
* Wed Jul 20 2016  Quentin GROLLEAU <quentin.grolleau@arkea.com> 0.9.5
- New version.
