%define name python-monasca-ui
%define pythonname monasca-ui
%define version 1.0.31
%define release 2

Summary:          Python Monasca UI
Name:             %{name}
Version:          %{version}
Release:          %{release}%{?dist}
License:          ASL 2.0
Group:            Development/Libraries
BuildRoot:        %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix:           %{_prefix}
BuildArch:        noarch
Vendor:           HP Cloud Monitoring <hpcs-mon@hp.com>
Url:              https://github.com/openstack/monasca-notification
Packager:         Quentin GROLLEAU <quentin.grolleau@arkea.com>

Source0:          https://pypi.python.org/packages/source/m/%{pythonname}/%{pythonname}-%{version}.tar.gz

Requires:         python-monascaclient
Requires:         python-django >= 1.8

BuildRequires:    python-setuptools python-devel python-pbr


%description
Monasca Plugin for Horizon

%prep
%setup -q -n %{pythonname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{python_sitelib}/*

%changelog
* Thu Jul 21 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 1.0.31-2
- New version

* Mon Feb 22 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 1.0.28-1.el7.centos
- Initial RPM
