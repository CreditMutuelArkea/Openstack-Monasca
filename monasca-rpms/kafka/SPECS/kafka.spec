%define name kafka
%define version 0.9.0.1
%define scala_version 2.11

Name:		%{name}
Version:	%{version}
Release:	1
Summary:	Apache kafka
Group:		Applications/System
License:	Apache Software License 2.0
URL:		http://kafka.apache.org
Packager:	Quentin GROLLEAU <quentin.grolleau@arkea.com>
Distribution:	ARKEA Linux
Vendor:		ARKEA
BuildArch: 	noarch

Source0:	%{name}_%{scala_version}-%{version}.tgz
Source1:	%{name}.service

Requires:	ArkeaOracleJDK8

Requires(pre): 	shadow-utils
Requires: 	systemd
BuildRequires: 	systemd

%description
Apache Kafka 0.9.0.1 with scala 2.11 

%prep

%setup -q -T -b 0 -n %{name}_%{scala_version}-%{version}

%build

%install
%{__mkdir} %{buildroot}/opt
%{__mkdir} %{buildroot}/opt/%{name}-%{version}
%{__cp} -r %{_builddir}/%{name}_%{scala_version}-%{version}/* %{buildroot}/opt/%{name}-%{version}
%{__mkdir} %{buildroot}/opt/%{name}-%{version}/data
%{__mkdir} %{buildroot}/opt/%{name}-%{version}/logs
%{__mkdir} %{buildroot}/opt/%{name}-%{version}/daemon

%{__mkdir_p} %{buildroot}%{_unitdir}
%{__install} %{SOURCE1} %{buildroot}%{_unitdir}/

%pre
getent group %{name} > /dev/null || groupadd -r %{name}
getent passwd %{name} > /dev/null || \
useradd -g %{name} -c "Apache kafka user" -M %{name} -d /opt/%{name} -s /bin/bash

%post
# Create symlink to new version
if [ ! -h /opt/%{name} ]; then
	%{__ln_s} /opt/%{name}-%{version} /opt/%{name}
fi

if [ $1 -eq 1 ]; then
/usr/bin/systemctl preset %{name}.service >/dev/null 2>&1 ||:
fi

%files
%defattr(755,%{name},%{name},755)
/opt/%{name}-%{version}
%{_unitdir}/%{name}.service
%doc

%preun
if [ $1 -eq 0 ]; then
/usr/bin/systemctl --no-reload disable %{name}.service >/dev/null 2>&1 ||:
/usr/bin/systemctl stop %{name}.service >/dev/null 2>&1 ||:
fi

%postun
/usr/bin/systemctl daemon-reload >/dev/null 2>&1 ||:
if [ $1 -ge 1 ]; then
	/sbin/service %{name} status  >/dev/null 2>&1 || exit 0
fi

%changelog
* Mon Jul 25 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 0.9.0.1-1.centos7
- New kafka version

