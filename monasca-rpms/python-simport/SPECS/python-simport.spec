%define name python-simport
%define pythonname simport
%define version 0.2.dev16
%define release 1

Summary:          Simple import with python path management
Name:             %{name}
Version:          %{version}
Release:          %{release}
Source0:          %{pythonname}-%{version}.tar.gz
License:          ASL 2.0
Group:            Development/Libraries
BuildRoot:        %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix:           %{_prefix}
BuildArch:        noarch
Vendor:           Dark Secret Software Inc. <admin@darksecretsoftware.com>
Url:              https://github.com/stackforge/stacktach-simport
Packager:         Quentin GROLLEAU <quentin.grolleau@arkea.com>

BuildRequires:    python-setuptools
BuildRequires:    python2-devel
BuildRequires:    python-pbr
BuildRequires:    python-sphinx


%description
Simport
  Simple Import Library for Python

  Supports importing functions or class methods from files
  not in the Python Path.

%prep
%setup -q -n %{pythonname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,)
%{python_sitelib}/*

%changelog
* Mon Feb 22 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 0.2.dev16-1.el7.centos
- Initial RPM
