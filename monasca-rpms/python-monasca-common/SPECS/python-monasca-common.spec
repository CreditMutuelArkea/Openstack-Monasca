%define name python-monasca-common
%define pythonname monasca-common
%define version 0.0.8
%define release 1

Summary:          Python Monasca Common
Name:             %{name}
Version:          %{version}
Release:          %{release}%{?dist}
License:          ASL 2.0
Group:            Development/Libraries
BuildRoot:        %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix:           %{_prefix}
BuildArch:        noarch
Vendor:           HP Cloud Monitoring <hpcs-mon@hp.com>
Url:              https://github.com/openstack/monasca-common
Packager:         Quentin GROLLEAU <quentin.grolleau@arkea.com>

Source0:          https://pypi.python.org/packages/source/m/%{pythonname}/%{pythonname}-%{version}.tar.gz

Requires:         python-iso8601
Requires:         kafka-python >= 0.9.5
Requires:         python-kazoo >= 2.0
Requires:         python-pbr
Requires:         python-six
Requires:         python-ujson >= 1.34
Requires:         python2-oslo-config
Requires:         python2-PyMySQL

BuildRequires:    python-setuptools
BuildRequires:    python2-devel
BuildRequires:    python-pbr
BuildRequires:    python-sphinx

%description
Python monasca-common is a collection of sub-projects containing reusable
application and platform code for building monitoring related services.

%prep
%setup -q -n %{pythonname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --root=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{python_sitelib}/*

%changelog
* Wed Jul 20 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 0.0.8-1.el7.centos
- New version
