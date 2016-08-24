%define name monasca-thresh
%define version 0.0.2
%define release 1

Summary:          Monasca Thresh
Name:             %{name}
Version:          %{version}
Release:          %{release}%{?dist}
License:          ASL 2.0
Group:            Development/Libraries
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix:           %{_prefix}
BuildArch:        noarch
Vendor:           Arkea Cloud
Packager:         Quentin GROLLEAU <quentin.grolleau@arkea.com>

Source0:          http://tarballs.openstack.org/ci/monasca-thresh/monasca-thresh-1.1.0-SNAPSHOT-shaded.jar
Source1:          thresh-config.yml
Source2:          monasca-thresh.service

Requires:         jdk-8u101-linux-x64

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
BuildRequires:    systemd

# Turn off strip'ng of binaries
%global __os_install_post %{nil}
%global __strip /bin/true

%description
Monasca-Thresh

%prep

%build

%install
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/monasca
%{__install} %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/monasca/monasca-thresh.jar
%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/monasca/thresh-config.yml
%{__mkdir_p} $RPM_BUILD_ROOT%{_unitdir}
%{__install} %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/log/monasca/thresh


%pre
getent group monasca >/dev/null || groupadd -r monasca
getent passwd mon-thresh >/dev/null || useradd -r -g monasca  -s /sbin/bash -c "Monasca Thresh user" mon-thresh

%files
%defattr(644,root,root,755)
%{_sysconfdir}/monasca/*
%attr(0644,mon-thresh,monasca) %{_unitdir}/monasca-thresh.service
%attr(0755,mon-thresh,monasca) %dir %{_localstatedir}/log/monasca/thresh

%changelog
* Fri Feb 19 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 0.1-1.el7.centos
- Initial RPM
