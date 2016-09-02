%define name python-pastedeploy
%define pythonname PasteDeploy
%define version 1.5.2
%define release 1

Summary:          Python PasteDeploy
Name:             %{name}
Version:          %{version}
Release:          %{release}
Source0:          %{pythonname}-%{version}.tar.gz
License:          ASL 2.0
Group:            Development/Libraries
BuildRoot:        %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix:           %{_prefix}
BuildArch:        noarch
Vendor:           Alex Gronholm
Url:              http://pythonpaste.org/deploy/
Packager:         Quentin GROLLEAU <quentin.grolleau@arkea.com>

Requires:  	  python-paste

BuildRequires:    python-setuptools python-devel python-pbr

%description
PasteDeploy
  Load, configure, and compose WSGI applications and servers

%prep
%setup -q -n %{pythonname}-%{version}

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
* Mon Apr 4 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 1.5.2-1.el7.centos
- Initial RPM
