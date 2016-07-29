%define name python-monasca-api
%define pythonname monasca-api
%define version 1.1.2
%define release 1

Summary:        Python Monasca Api
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
License:        ASL 2.0
Group:          Development/Libraries
BuildRoot:      %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix:         %{_prefix}
BuildArch:      noarch
Vendor:         HP Cloud Monitoring <hpcs-mon@hp.com>
Url:            https://github.com/openstack/monasca-api
Packager:       Quentin GROLLEAU <quentin.grolleau@arkea.com>


Source0:        https://pypi.python.org/packages/source/m/%{pythonname}/%{pythonname}-%{version}.tar.gz
Source1:        %{pythonname}.service

# << Patch Arkea
Patch0:         idle_timeout.patch
# >> Patch Arkea

Requires:         python2-eventlet
Requires:         python-falcon
Requires:         python-gunicorn >= 19.1.0
Requires:         python-influxdb
Requires:         kafka-python
Requires:         python-keystonemiddleware
Requires:         python-monasca-common >= 0.0.2
Requires:         python2-oslo-config
Requires:         python-oslo-log
Requires:         python-oslo-middleware
Requires:         python2-oslo-serialization
Requires:         python2-oslo-utils
Requires:         python-paste-deploy
Requires:         python-pbr
Requires:         pyparsing
Requires:         python-dateutil
Requires:         python-keystoneclient
Requires:         python-simplejson
Requires:         python-simport
Requires:         python-six
Requires:         python-ujson >= 1.33
Requires:         python-validate-email >= 1.3
Requires:         python-voluptuous


Requires(pre):    shadow-utils
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
BuildRequires:    systemd
BuildRequires:    python-setuptools python-devel python-pbr

%description
Monitoring Api
  The Monasca API provides a RESTful JSON interface for interacting with and
  managing monitoring related resources.

%prep
%setup -q -n %{pythonname}-%{version}

%patch0 -p1

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=$RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/log/monasca/api
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/run/monasca/api
%{__mkdir_p} $RPM_BUILD_ROOT%{_unitdir}
%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/

%pre
getent group monasca >/dev/null || groupadd -r monasca
getent passwd mon-api >/dev/null || useradd -M -r -g monasca -s /bin/bash -c "Monasca Api user" --home /etc/monasca/ mon-api

%post
%systemd_post %{pythonname}.service

%preun
%systemd_preun %{pythonname}.service

%postun
%systemd_postun_with_restart %{pythonname}.service

%files
%defattr(644,root,root,755)
%{_unitdir}/monasca-api.service
%{_bindir}/monasca-api
%{_sysconfdir}/monasca/*
%{python_sitelib}/*
%attr(0755,mon-api,monasca) %dir %{_localstatedir}/log/monasca/api
%attr(0755,-,monasca) %dir %{_localstatedir}/run/monasca/api

%changelog
* Thu Jul 21 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 1.1.2-1
- New version

