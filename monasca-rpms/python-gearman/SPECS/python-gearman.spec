%define name python-gearman
%define pythonname gearman
%define version 2.0.2
%define release 1

Summary:          Gearman API
Name:             %{name}
Version:          %{version}
Release:          %{release}%{?dist}
License:          ASL 2.0
Group:            Development/Libraries
BuildRoot:        %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix:           %{_prefix}
BuildArch:        noarch
Url:              http://github.com/Yelp/python-gearman/
Packager:         Quentin GROLLEAU <quentin.grolleau@arkea.com>

Source0:          https://pypi.python.org/packages/source/g/%{pythonname}/%{pythonname}-%{version}.tar.gz

BuildRequires:    python-setuptools
BuildRequires:    python2-devel
BuildRequires:    python-pbr
BuildRequires:    python-sphinx

%description
Gearman API - Client, worker, and admin client interfaces.

%prep
%setup -q -n %{pythonname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=$RPM_BUILD_ROOT

%pre

%files
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
* Wed Jul 20 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 2.0.2-1.el7.centos
- Initial RPM
