%define name python-monascaclient
%define version 1.0.30
%define release 1

Summary:          Monasca API Client Library
Name:             %{name}
Version:          %{version}
Release:          %{release}%{?dist}
License:          ASL 2.0
Group:            Development/Libraries
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix:           %{_prefix}
BuildArch:        noarch
Vendor:           HP Cloud Monitoring <hpcs-mon@hp.com>
Url:              https://github.com/openstack/python-monascaclient
Packager:         Quentin GROLLEAU <quentin.grolleau@arkea.com>

Source0:          %{name}-%{version}.tar.gz

Requires:         python2-iso8601 >= 0.1.9
Requires:         python2-oslo-config
Requires:         python2-oslo-i18n
Requires:         python2-oslo-serialization
Requires:         python2-oslo-utils
Requires:         python-argparse >= 1.4.0
Requires:         python-babel
Requires:         python-keystoneclient
Requires:         python-oslo-concurrency
Requires:         python-oslo-log
Requires:         python-oslo-middleware
Requires:         python-oslo-service
Requires:         python-pbr >= 0.11
Requires:         python-prettytable >= 0.7
Requires:         python-requests >= 1.1
Requires:         python-six >= 1.7.0
Requires:         PyYAML >= 3.1.0

BuildRequires:    python-setuptools python-devel python-pbr

%description
Python bindings to the Monasca API
  This is a client library for Monasca built to interface with the Monasca API.
  It provides a Python API (the monascaclient module) and a command-line tool
  (monasca).

%prep
%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{python_sitelib}/*
%{_datarootdir}/monasca.bash_completion
%attr(0755,root,root) %{_bindir}/*

%changelog
* Mon Apr 11 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 1.0.30-1
- new version for mitaka
