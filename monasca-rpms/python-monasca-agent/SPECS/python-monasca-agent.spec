%define name python-monasca-agent
%define pythonname monasca-agent
%define version 1.1.24
%define release 1

Summary:        Python Monasca Agent
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
License:        ASL 2.0
Group:          Development/Libraries
BuildRoot:      %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix:         %{_prefix}
BuildArch:      noarch
Vendor:         HP Cloud Monitoring <hpcs-mon@hp.com>
Url:            https://github.com/openstack/monasca-agent
Packager:       Quentin GROLLEAU <quentin.grolleau@arkea.com>


Source0:        https://pypi.python.org/packages/source/m/%{pythonname}/%{pythonname}-%{version}.tar.gz
Source1:        %{pythonname}.service
Source2:        supervisor.conf
Source3:        agent.yaml.template

Patch0:		util.py.patch	

Requires:       python2-oslo-config
Requires:       python2-oslo-i18n
Requires:       python2-oslo-serialization
Requires:       python2-oslo-utils
Requires:       python-gearman >= 2.0.2
Requires:       python-httplib2
Requires:       python-pymongo
Requires:       python-meld3
Requires:       python-memcached
Requires:       python-monascaclient >= 1.0.30
Requires:       python-netaddr
Requires:       python-ntplib >= 0.3.2
Requires:       python-oslo-concurrency
Requires:       python-oslo-log
Requires:       python-oslo-middleware
Requires:       python-oslo-vmware
Requires:       python-psutil
Requires:       python-redis
Requires:       python-requests
Requires:       python-simplejson
Requires:       python-tornado
Requires:       PyYAML
Requires:       supervisor >= 3.1.3

Requires(pre):    shadow-utils
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
BuildRequires:    systemd
BuildRequires:    python-setuptools python-devel python-pbr


%description
Monitoring Agent
 The Monitoring Agent is a lightweight process that monitors system
 processes and services, and sends information
 back to your OpenStack monitoring Account.

 This package installs and runs the advanced Agent daemon, which queues and
 forwards metrics from your applications as well as system services.

%prep
%setup -q -n %{pythonname}-%{version}

%patch0 -p1

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=$RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/monasca/agent/conf.d
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/log/monasca/agent
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/run/monasca
%{__install} %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/monasca/agent/
%{__install} %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/monasca/agent/
%{__mkdir_p} $RPM_BUILD_ROOT%{_unitdir}
%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/

%pre
getent group monasca >/dev/null || groupadd -r monasca
getent passwd mon-agent >/dev/null || useradd -M -r -g monasca -s /bin/bash -c "Monasca Agent user" --home /etc/monasca/agent mon-agent

%post
%systemd_post %{pythonname}.service

%preun
%systemd_preun %{pythonname}.service

%postun
%systemd_postun_with_restart %{pythonname}.service

%files
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/monasca/agent/*
%{_unitdir}/monasca-agent.service
%{python_sitelib}/*
%{_datarootdir}/monasca/agent/*
%attr(0755,mon-agent,monasca) %dir %{_localstatedir}/log/monasca/agent
%attr(0755,mon-agent,monasca) %dir %{_localstatedir}/run/monasca
%attr(0755,root,root) %{_bindir}/*
