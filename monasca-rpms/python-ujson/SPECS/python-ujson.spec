%define name python-ujson
%define pythonname ujson
%define version 1.35
%define release 1

Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        An ultra fast JSON encoder and decoder written in pure C

Group:          Development/Libraries
License:        BSD
URL:            http://pypi.python.org/pypi/%{pythonname}

Source0:        http://pypi.python.org/packages/source/u/%{pythonname}/%{pythonname}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-tools


%description
UltraJSON is an ultra fast JSON encoder and decoder written in
pure C with bindings for Python

%prep
%setup -qn %{pythonname}-%{version}
# Remove egg-info
rm -rf *.egg-info

%build
python setup.py build

%install
# If we install with --skip-build the build directory containing the C
# extensions are deleted before the install. So, nothing install besides the
# egg-info. See: https://github.com/esnme/ultrajson/issues/179
python setup.py install -O1 --root %{buildroot}

%files -n %{name}
%doc README.rst
%{python2_sitearch}/%{pythonname}-%{version}-py%{python2_version}.egg-info/
%{python2_sitearch}/%{pythonname}.so


%changelog
* Wed Jul 20 2016 Quentin GROLLEAU <quentin.grolleau@arkea.com> - 1.35-1
- New version

