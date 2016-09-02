%define name python-nose-cov
%define pythonname nose-cov
%define version 1.6
%define release 1

Summary:          Nose plugin
Name:             %{name}
Version:          %{version}
Release:          %{release}
Source0:          %{pythonname}-%{version}.tar.gz
License:          ASL 2.0
Group:            Development/Libraries
BuildRoot:        %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix:           %{_prefix}
BuildArch:        noarch
Url:              http://bitbucket.org/memedough/nose-cov/overview
Packager:         Quentin GROLLEAU <quentin.grolleau@arkea.com>

BuildRequires:    python-setuptools python-devel python-pbr

%description
Nose plugin for coverage reporting, including subprocesses and multiprocessing
This plugin produces coverage reports.
It also supports coverage of subprocesses.

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
* Thu Jul 21 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 1.6-1.el7.centos
- Initial RPM
