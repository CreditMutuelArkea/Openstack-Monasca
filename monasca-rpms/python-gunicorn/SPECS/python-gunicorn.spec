
%global upstream_name gunicorn
%global name python-gunicorn
%global version 19.6.0
%global release 1

Summary:        Python WSGI application server
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}

Group:          System Environment/Daemons
License:        MIT
URL:            http://gunicorn.org/
Source0:        http://pypi.python.org/packages/source/g/%{upstream_name}/%{upstream_name}-%{version}.tar.gz


BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  pytest
BuildRequires:  python-mock
BuildRequires:  python-pytest-cov
BuildRequires:  python-sphinx
BuildRequires:  python-sphinx_rtd_theme


Requires:       python-setuptools

%description
Gunicorn ("Green Unicorn") is a Python WSGI HTTP server for UNIX. It uses the
pre-fork worker model, ported from Ruby's Unicorn project. It supports WSGI,
Django, and Paster applications.


%package doc
Summary:        Documentation for the %{name} package

%description doc
Documentation for the %{name} package.

%prep
%setup -q -n %{upstream_name}-%{version}


# need to remove gaiohttp worker from the Python 2 version, it is supported on
# Python 3 only and it fails byte compilation on 2.x due to using "yield from"
rm gunicorn/workers/_gaiohttp.py*

%build
%{__python} setup.py build
%{__python} setup.py build_sphinx

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc LICENSE NOTICE README.rst THANKS
%{python_sitelib}/%{upstream_name}*
%{_bindir}/%{upstream_name}
%{_bindir}/%{upstream_name}_django
%{_bindir}/%{upstream_name}_paster


%files doc
%doc LICENSE build/sphinx/html/*

%changelog
* Wed Jul 20 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 19.6.0-1
- New version for monasca-api
