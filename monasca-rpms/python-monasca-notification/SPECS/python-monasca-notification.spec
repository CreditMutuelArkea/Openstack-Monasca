%define name python-monasca-notification
%define pythonname monasca-notification
%define version 1.2.13
%define release 1

Summary:          Python Monasca Notification
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
Source1:          %{pythonname}.service
Source2:          notification.yaml.template


Requires:         python-monasca-common
Requires:         python-monasca-statsd
Requires:         python-pbr
Requires:         python-requests
Requires:         python-simport 
Requires:         python-six
Requires:         PyYAML

Requires(pre):    shadow-utils
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

BuildRequires:    systemd
BuildRequires:    python-setuptools python-devel python-pbr


%description
This engine reads alarms from Kafka and then notifies the customer using their
configured notification method.Multiple notification and retry engines can run
in parallel up to one per available Kafka partition.
Zookeeper is used to negotiate access to the Kafka partitions whenever a
new process joins or leaves the working set.

%prep
%setup -q -n %{pythonname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=$RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/log/monasca/notification
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/monasca
%{__install} %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/monasca
%{__mkdir_p} $RPM_BUILD_ROOT%{_unitdir}
%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/

%pre
getent group monasca >/dev/null || groupadd -r monasca
getent passwd mon-notification >/dev/null || useradd -r -g monasca  -s /bin/bash -c "Monasca Agent user" mon-notification

%post
%systemd_post %{pythonname}.service

%preun
%systemd_preun %{pythonname}.service

%postun
%systemd_postun_with_restart %{pythonname}.service

%files
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/monasca/*
%{_unitdir}/monasca-notification.service
%{python_sitelib}/*
%attr(0755,mon-notification,monasca) %dir %{_localstatedir}/log/monasca/notification
%attr(0755,root,root) %{_bindir}/*

%changelog
* Mon Feb 22 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 1.1.23-1.el7.centos
- Initial RPM
