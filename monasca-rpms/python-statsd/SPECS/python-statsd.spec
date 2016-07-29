%define name python-statsd
%define version 2.0.0
%define release 1

Summary:          A Python statsd client
Name:             %{name}
Version:          %{version}
Release:          %{release}%{?dist}

License:          BSD
URL:              https://github.com/WoLpH/python-statsd
Source0:          https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    python-setuptools python-devel python-pbr

%description
A python client for the statsd daemon.

%prep
%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=$RPM_BUILD_ROOT

%files 
%{python_sitelib}/*


%changelog
* Thu Jul 21 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 2.0.0-1
- Initial rpm

