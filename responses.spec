#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : responses
Version  : 0.10.7
Release  : 12
URL      : https://files.pythonhosted.org/packages/df/be/e3c18220cf8ed5ace9ac3e2de28a46e4994ddefe9e61fe3b3971a1bc20fe/responses-0.10.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/df/be/e3c18220cf8ed5ace9ac3e2de28a46e4994ddefe9e61fe3b3971a1bc20fe/responses-0.10.7.tar.gz
Summary  : A utility library for mocking out the `requests` Python library.
Group    : Development/Tools
License  : Apache-2.0
Requires: responses-license = %{version}-%{release}
Requires: responses-python = %{version}-%{release}
Requires: responses-python3 = %{version}-%{release}
Requires: cookies
Requires: requests
Requires: six
BuildRequires : Werkzeug
BuildRequires : buildreq-distutils3
BuildRequires : cookies
BuildRequires : coverage
BuildRequires : flake8
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytest-cov
BuildRequires : pytest-localserver
BuildRequires : python-mock
BuildRequires : requests
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
=========

%package license
Summary: license components for the responses package.
Group: Default

%description license
license components for the responses package.


%package python
Summary: python components for the responses package.
Group: Default
Requires: responses-python3 = %{version}-%{release}

%description python
python components for the responses package.


%package python3
Summary: python3 components for the responses package.
Group: Default
Requires: python3-core

%description python3
python3 components for the responses package.


%prep
%setup -q -n responses-0.10.7
cd %{_builddir}/responses-0.10.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575330214
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/responses
cp %{_builddir}/responses-0.10.7/LICENSE %{buildroot}/usr/share/package-licenses/responses/cef33b64c628a8301c7f0a1d2360484b9fe5bed1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/responses/cef33b64c628a8301c7f0a1d2360484b9fe5bed1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
