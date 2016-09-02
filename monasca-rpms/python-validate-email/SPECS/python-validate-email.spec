%define name python-validate-email
%define pythonname validate_email
%define version 1.3
%define release 1

Summary:          Python Validate Email
Name:             %{name}
Version:          %{version}
Release:          %{release}
Source0:          %{pythonname}-%{version}.tar.gz
License:          ASL 2.0
Group:            Development/Libraries
BuildRoot:        %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix:           %{_prefix}
BuildArch:        noarch
Vendor:           Syrus Akbary
Url:              http://github.com/syrusakbary/%{pythonname}
Packager:         Quentin GROLLEAU <quentin.grolleau@arkea.com>

BuildRequires:    python-setuptools python-devel python-pbr

%description
Validate_email verify if an email address is valid and really exists.

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
* Mon Apr 4 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 1.3-1.el7.centos
- Initial RPM
