%define name python-monasca-persister
%define pythonname monasca-persister
%define version 0.1.15
%define release 1

Summary:          Python Monasca persister
Name:             %{name}
Version:          %{version}
Release:          %{release}%{?dist}
License:          ASL 2.0
Group:            Development/Libraries
BuildRoot:        %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix:           %{_prefix}
BuildArch:        noarch
Vendor:           HP Cloud Monitoring <hpcs-mon@hp.com>
Url:              https://github.com/openstack/monasca-persister
Packager:         Quentin GROLLEAU <quentin.grolleau@arkea.com>


Source0:          https://pypi.python.org/packages/source/m/%{pythonname}/%{pythonname}-%{version}.tar.gz
Source1:          %{pythonname}.service

## https://review.openstack.org/#/c/343534/
Patch0:		  setup.cfg-343534.patch
Patch1:		  monasca-persister_repositories_influxdb.patch

Requires:         python2-babel
Requires:         python-influxdb == 2.8.0
Requires:         python-iso8601
Requires:         python-monasca-common
Requires:         python2-oslo-config
Requires:         python2-oslo-service
Requires:         python-oslo-log
Requires:         python-simport
Requires:         python-six >= 1.9.0


Requires(pre):    shadow-utils
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
BuildRequires:    systemd
BuildRequires:    python-setuptools python-devel python-pbr

%description
Monitoring persister
  The Monasca persister provides a RESTful JSON interface for interacting with
  and managing monitoring related resources.

%prep
%setup -q -n %{pythonname}-%{version}

%patch0 -p1
%patch1 -p1

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=$RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/log/monasca/persister
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/run/monasca/persister
%{__mkdir_p} $RPM_BUILD_ROOT%{_unitdir}
%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/

%pre
getent group monasca >/dev/null || groupadd -r monasca
getent passwd mon-persister >/dev/null || useradd -r -g monasca -s /bin/bash -c "Monasca persister user" mon-persister

%post
%systemd_post %{pythonname}.service

%preun
%systemd_preun %{pythonname}.service

%postun
%systemd_postun_with_restart %{pythonname}.service

%files
%defattr(644,root,root,755)
%{_unitdir}/monasca-persister.service
%attr(0755,mon-persister,monasca) %{_bindir}/monasca-persister
%{python_sitelib}/*
%attr(0755,mon-persister,monasca) %dir %{_localstatedir}/log/monasca/persister
%attr(0755,mon-persister,monasca) %dir %{_localstatedir}/run/monasca/persister
