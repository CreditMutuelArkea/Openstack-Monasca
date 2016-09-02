%define name python-dateutil
%define pythonname dateutil
%define version 2.5.3
%define release 1

Summary:          Extensions to the standard Python datetime module
Name:             %{name}
Version:          %{version}
Release:          %{release}
Source0:          %{name}-%{version}.tar.gz
License:          ASL 2.0
Group:            Development/Libraries
BuildRoot:        %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix:           %{_prefix}
BuildArch:        noarch
Url:              https://dateutil.readthedocs.org
Packager:         Quentin GROLLEAU <quentin.grolleau@arkea.com>

BuildRequires:    python-setuptools python-devel python-pbr

%description
The dateutil module provides powerful extensions to the datetime module
available in the Python standard library.

%prep
%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,)
%{python_sitelib}/*

%changelog
* Thu Jul 21 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 2.5.3-1.el7.centos
- Initial RPM
