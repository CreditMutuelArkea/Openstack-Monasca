%define name zookeeper
%define version 3.4.8
%define release 1
%define user zk
%define user_group zk

Summary:          Apache ZooKeeper
Name:             %{name}
Version:          %{version}
Release:          %{release}%{?dist}
License:          ASL 2.0
Group:            Applications/Databases
URL:              http://zookeeper.apache.org
Packager:         Quentin GROLLEAU <quentin.grolleau@arkea.com>
Distribution:     ARKEA Linux
Vendor:           ARKEA

Source0:          http://apache.mirrors.ovh.net/ftp.apache.org/dist/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:          %{name}.service
Source2:          %{name}.sysconfig

Requires:         ArkeaOracleJDK8

Requires(pre):    shadow-utils
Requires:         systemd
BuildRequires:    systemd

%description
Apache ZooKeeper is an effort to develop and maintain an open-source server
which enables highly reliable distributed coordination.

%prep
%setup -q -T -c -a 0

%build

%install
%{__mkdir} $RPM_BUILD_ROOT/opt
%{__mkdir} $RPM_BUILD_ROOT/opt/%{name}-%{version}
%{__cp} -r %{name}-%{version} $RPM_BUILD_ROOT/opt/
%{__mkdir} $RPM_BUILD_ROOT/opt/%{name}-%{version}/data
%{__mkdir} $RPM_BUILD_ROOT/opt/%{name}-%{version}/log
%{__mkdir} $RPM_BUILD_ROOT/opt/%{name}-%{version}/logs
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}
cd $RPM_BUILD_ROOT/opt
%{__ln_s} %{name}-%{version} %{name}

%{__mkdir_p} $RPM_BUILD_ROOT%{_unitdir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/
%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/
%{__install} %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}


%clean
# Delete current version if it has been previously installed
rm -rf $RPM_BUILD_ROOT/opt/%{name}-%{version}

%pre
getent group %{user_group} > /dev/null || groupadd -r %{user_group}
getent passwd %{user} > /dev/null || \
useradd -g %{user_group} -c "Apache zookeeper user" -M %{user} -d /opt/%{name} -s /bin/bash

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart my.service

%files

%defattr(644,%{user},%{user},755)
/opt/%{name}-%{version}
/opt/%{name}

%defattr(755,%{user},%{user},755)
/opt/%{name}-%{version}/bin
%{_localstatedir}/log/%{name}

%{_unitdir}/%{name}.service
%{_sysconfdir}/sysconfig/zookeeper
%doc

%changelog
* Wed Jul 13 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 3.4.8-1.el7.centos
- Migration to 3.4.8
