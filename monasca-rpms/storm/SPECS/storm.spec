%define name storm
%define apachename apache-storm
%define version 0.9.6 
%define release 1
%define storm_user storm
%define storm_group storm

Summary:        Storm Complex Event Processing
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
License:        ASL 2.0
Group:          Development/Libraries
BuildRoot:      %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix:         %{_prefix}
BuildArch:      noarch
Url:            http://storm-project.net
Packager:       Quentin GROLLEAU <quentin.grolleau@arkea.com>

Source0:        http://apache.mirrors.tds.net/%{name}/%{apachename}-%{version}/%{apachename}-%{version}.tar.gz
Source1:        %{name}-logviewer.service
Source2:        %{name}-nimbus.service
Source3:        %{name}-supervisor.service
Source4:        %{name}-ui.service

Requires(pre):    shadow-utils
Requires:         systemd
BuildRequires:    systemd

%description
Storm is a distributed realtime computation system.
Storm provides a set of general primitives for doing realtime computation.
Storm is simple, can be used with any programming language, is used by many
companies, and is a lot of fun to use!

%prep
%setup -q -n %{apachename}-%{version}

# This SPEC build is Only Packaging.
%build

%install
%{__mkdir_p} %{buildroot}/opt/%{name}-%{version}
%{__cp} -r %{_builddir}/%{apachename}-%{version}/* %{buildroot}/opt/%{name}-%{version}
cd %{buildroot}/opt
%{__ln_s} %{name}-%{version} %{name}
%{__mkdir_p} %{buildroot}%{_unitdir}
%{__install} %{SOURCE1} %{buildroot}%{_unitdir}/
%{__install} %{SOURCE2} %{buildroot}%{_unitdir}/
%{__install} %{SOURCE3} %{buildroot}%{_unitdir}/
%{__install} %{SOURCE4} %{buildroot}%{_unitdir}/

%clean
rm -rf %{buildroot}/opt/%{name}-%{version}

%pre
getent group %{storm_group} >/dev/null || groupadd -r %{storm_group}
getent passwd %{storm_user} >/dev/null || /usr/sbin/useradd --comment "Storm Daemon User" --shell /bin/bash -M -r -g %{storm_group} --home /opt/storm %{storm_user}

%post
%systemd_post %{name}-logviewer.service
%systemd_post %{name}-nimbus.service
%systemd_post %{name}-supervisor.service
%systemd_post %{name}-ui.service

%preun
%systemd_preun %{name}-logviewer.service
%systemd_preun %{name}-nimbus.service
%systemd_preun %{name}-supervisor.service
%systemd_preun %{name}-ui.service

%postun
%systemd_postun %{name}-logviewer.service
%systemd_postun %{name}-nimbus.service
%systemd_postun %{name}-supervisor.service
%systemd_postun %{name}-ui.service

%files
%defattr(-,%{storm_user},%{storm_group},-)
/opt/%{name}-%{version}
/opt/%{name}
%{_unitdir}/%{name}-logviewer.service
%{_unitdir}/%{name}-nimbus.service
%{_unitdir}/%{name}-supervisor.service
%{_unitdir}/%{name}-ui.service
%doc

%defattr(755,%{storm_user},%{storm_group},755)
/opt/%{name}-%{version}/bin/*
