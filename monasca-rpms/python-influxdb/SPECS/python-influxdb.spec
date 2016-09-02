%define name python-influxdb
%define pythonname influxdb
%define version 2.8.0 
%define release 1

Summary:          InfluxDB client
Name:             %{name}
Version:          %{version}
Release:          %{release}%{?dist}
License:          ASL 2.0
Group:            Development/Libraries
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix:           %{_prefix}
BuildArch:        noarch
Url:              https://pypi.python.org/pypi/influxdb
Packager:         Quentin GROLLEAU <quentin.grolleau@arkea.com>

Source0:          %{pythonname}-%{version}.tar.gz

Requires:         python-requests-mock
Requires:         python-nose-cov
Requires:         python-nose
Requires:         python-mock
Requires:         python-six >= 1.9.0
Requires:         python-requests >= 1.0.3
Requires:         pytz
Requires:         python-dateutil >= 2.0.0

BuildRequires:    python-setuptools
BuildRequires:    python2-devel
BuildRequires:    python-pbr
BuildRequires:    python-sphinx

%description
API bindings for InfluxDB.
  Supports both InfluxDB v0.8 and InfluxDB >= 0.9.
  InfluxDB is an open source distributed time series database with no external
  dependencies. It's useful for recording metrics, events, and performing
  analytics.

%prep
%setup -q -n %{pythonname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --root=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{python_sitelib}/*

%changelog
* Wed Jul 20 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 2.8.0-1.el7.centos
- New version
