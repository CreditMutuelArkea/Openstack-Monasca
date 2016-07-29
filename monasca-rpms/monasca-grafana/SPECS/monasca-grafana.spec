%define name hpcloud-mon-grafana
%define version 1.5.4
%define release 1

Summary:          Monasca Grafana
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

Source0:          %{name}-v1.5.4-918.tar.gz


%description
Monasca-Grafana
  This package is going to install the monasca-grafana

%prep
%setup -n hpcloud-mon-grafana-ebbf9e7

%build

%install
%{__mkdir_p} $RPM_BUILD_ROOT%{_datarootdir}/%{name}
%{__cp} -r %{_builddir}/hpcloud-mon-grafana-ebbf9e7/* $RPM_BUILD_ROOT%{_datarootdir}/%{name}
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/www/html/grafana
%{__cp} -r %{_builddir}/hpcloud-mon-grafana-ebbf9e7/src/* $RPM_BUILD_ROOT%{_localstatedir}/www/html/grafana

%files
%defattr(644,root,root,755)
%{_datarootdir}/hpcloud-mon-grafana/*
%{_localstatedir}/www/html/grafana/*

%changelog
* Mon Feb 22 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 1.5.4-1.el7.centos
- Initial RPM
